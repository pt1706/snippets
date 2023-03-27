import asyncio
import logging

import aiohttp
from aiohttp import ClientSession

from async_book.util import async_timed


@async_timed()
async def fetch_status(
        session: ClientSession,
        url: str,
        delay: int = 0
) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://www.vk.com'
        pending = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url))
        ]
        while pending:
            done, pending = await asyncio.wait(pending,
                                               return_when=asyncio.FIRST_COMPLETED)
            print(f'Число завершившихся задач: {len(done)}')
            print(f'Число ожидающих задач: {len(pending)}')
            for done_task in done:
                print(await done_task)

asyncio.run(main())