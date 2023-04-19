import math


def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    return math.log2(n) - round(math.log2(n)) == 0


if __name__ == '__main__':
    assert True is isPowerOfTwo(16), 'test 1'
    assert False is isPowerOfTwo(6), 'test 2'
    assert False is isPowerOfTwo(0), 'test 3'
    assert False is isPowerOfTwo(-16), 'test 4'