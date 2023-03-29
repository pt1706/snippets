import asyncio
import aiohttp


from async_book.util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://www.vk.com', delay=1),
                    fetch_status(session, 'https://www.vk.com', delay=1),
                    fetch_status(session, 'https://www.vk.com', delay=10)]
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)

asyncio.run(main())