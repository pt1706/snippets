import aiohttp
from aiohttp import ClientSession

from async_book.util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = aiohttp.ClientTimeout(total=300)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status