import asyncio

import aiohttp

from async_book.util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = \
            [asyncio.create_task(fetch_status(session, 'https://vk.com', delay=1)),
             asyncio.create_task(fetch_status(session, 'https://vk.com', delay=5)),
             asyncio.create_task(fetch_status(session, 'htt://vk.com', delay=0))]

        done, pending = await asyncio.wait(
            fetchers,
            return_when=asyncio.FIRST_COMPLETED
        )
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        while pending:
            done, pending = await asyncio.wait(
                pending,
                return_when=asyncio.FIRST_COMPLETED
            )
            print(f'Число завершившихся задач: {len(done)}')
            print(f'Число ожидающих задач: {len(pending)}')

            for done_task in done:
                if done_task.exception() is None:
                    print(done_task.result())
                else:
                    pass

asyncio.run(main())