import asyncio

import aiohttp
from aiohttp import ClientSession

from async_book.util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str, t_o: int = 300, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    t_o = aiohttp.ClientTimeout(total=t_o)
    async with session.get(url, timeout=t_o) as result:
        return result.status