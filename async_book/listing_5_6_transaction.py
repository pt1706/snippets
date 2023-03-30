import logging

import asyncpg
import asyncio

from async_book.util import async_timed


product_query = \
    """
    SELECT
    p.product_id,
    p.product_name,
    p.brand_id,
    s.sku_id,
    pc.product_color_name,
    ps.product_size_name
    FROM product as p
    JOIN sku as s on s.product_id = p.product_id
    JOIN product_color as pc on pc.product_color_id = s.product_color_id
    JOIN product_size as ps on ps.product_size_id = s.product_size_id
    WHERE p.product_id = 100
    """


async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


@async_timed()
async def query_products_synchronously(pool, queries):
    return [await query_product(pool) for _ in range(queries)]


@async_timed()
async def query_products_concurrently(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)


@async_timed()
async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='product',
    )
    async with connection.transaction():
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'my_new_brand')")
        try:
            async with connection.transaction():
                await connection.execute("INSERT INTO product_color VALUES(1, 'black')")
        except Exception as ex:
            logging.warning('Ошибка при вставке цвета товара игнорируется', exc_info=ex)
    await connection.close()

asyncio.run(main())