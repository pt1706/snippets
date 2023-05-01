from functools import reduce


def addDigits(num: int) -> int:
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    else:
        return num % 9


def addDigits_simple(num: int) -> int:
    if num <= 9:
        return num
    num = reduce(lambda x, y: x + y, map(int, str(num)))
    return addDigits(num)


if __name__ == '__main__':
    num = 38
    assert 2 == addDigits(num), 'test 1'