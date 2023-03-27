import asyncio

from async_book.util import delay, async_timed


@async_timed()
async def slow_func(a: int, b: int) -> int:
    max = 0
    for i in range(a + 1):
        for j in range(b + 1):
            if max < a * b:
                max = a * b
    return max


@async_timed()
async def main(*args):
    sleep_for_three = asyncio.create_task(delay(3))
    do_slow_func = asyncio.create_task(slow_func(*args))

    try:
        res = await asyncio.wait_for(sleep_for_three, timeout=4)
        print('sleep_for_three: ', res)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        print(f'Задача была снята? {sleep_for_three.cancelled()}')

    res = await do_slow_func
    print('do_slow_func: ', res)


if __name__ == '__main__':
    asyncio.run(main(5000, 5000))
