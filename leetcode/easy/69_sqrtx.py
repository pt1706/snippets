from typing import Callable


def mySqrt(x: int) -> int:
    left = 0
    right = x
    while (right - left) > 1:
        mid = (right + left) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            left = mid
        if mid * mid > x:
            right = mid
    if right * right <= x:
        return right
    return left


def mySqrt_long(x: int) -> int:
    left = 0
    right = x
    while True:
        mid = ((right - left) // 2) + left
        if mid * mid == x:
            return mid
        if mid * mid < x:
            if (mid + 1) ** 2 == x:
                return mid + 1
            if (mid + 1) ** 2 > x:
                return mid
            left = mid
        if mid * mid > x:
            if (mid - 1) ** 2 <= x:
                return mid - 1
            right = mid


def test(f: Callable) -> None:
    for case in cases:
        assert case[0] == f(case[1])
    print(f'tests of func: {f.__name__} - passed')


if __name__ == '__main__':
    cases = [
        (1, 1),
        (12, 145),
        (13, 180),
        (14, 196),
        (15, 240),
        (3, 10),
        (2, 4),
        (2, 8),
        (0, 0),
    ]
    test(mySqrt)
    test(mySqrt_long)