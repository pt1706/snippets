def isUgly(n: int) -> bool:
    if n <= 0:
        return False
    while n == 1 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        if n % 5 == 0:
            n = n / 5
        if n % 3 == 0:
            n = n / 3
        if n % 2 == 0:
            n = n / 2
        if n == 1:
            return True
    return False


def isUgly_shorter(n: int) -> bool:
    if n <= 0:
        return False
    for div in (2, 3, 5):
        while n == 1 or n % div == 0:
            if n % div == 0:
                n = n / div
            if n == 1:
                return True
    return False


if __name__ == '__main__':
    n = 6
    assert True is isUgly(n), 'test 1'

    n = 14
    assert False is isUgly(n), 'test 2'

    n = 25
    assert True is isUgly(n), 'test 3'

    n = 1
    assert True is isUgly(n), 'test 4'