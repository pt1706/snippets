from random import sample
from typing import List, Tuple, Union

import asyncpg
import asyncio


from async_book.util import async_timed


def load_common_words() -> List[str]:
    with open('async_book/common_words.txt') as common_words:
        return common_words.readlines()


def generate_brand_names(words: List[str]) -> List[Tuple[Union[str, ]]]:
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_brands, brands)


@async_timed()
async def main():
    common_words = load_common_words()
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='product',
    )
    await insert_brands(common_words, connection)
    await connection.close()

asyncio.run(main())