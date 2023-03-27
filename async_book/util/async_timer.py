import functools
import time
from typing import Callable, Any


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(
                f'Func: <<{func.__name__}>> '
                f'executed with args: {args}, kwargs: {kwargs}'
            )
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                print(
                    f'Func: <<{func.__name__}>> finished, time of execution: '
                    f'{(time.time() - start):07.3f} s'
                )
        return wrapped
    return wrapper