import asyncio
import aiohttp

from async_book.util import async_timed, fetch_status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://vk.com' for _ in range(100)]
        status_codes = [await fetch_status(session, url) for url in urls]
        print(status_codes)


asyncio.run(main())