from functools import reduce


def my_factor(n: int) -> int:
    msg = 'factorial not defined for negative values'
    if n <= 0:
        raise ValueError(msg)
    lst = list(range(1, n + 1))
    return reduce(lambda x, y: x * y, lst)


if __name__ == '__main__':
    assert my_factor(6) == 720
    assert my_factor(7) == 5040

    try:
        my_factor(-7)
    except ValueError as error:
        assert error.args[0] == 'factorial not defined for negative values'

    print('all tests passed')


# ------------------ 2 ---------------------


lst = list(range(1, 11))

std_reduce = reduce(lambda x, y: x + y**2, lst)


def my_reduce(lst):
    res = 0
    for x in lst:
        res += x ** 2
    return res


if __name__ == '__main__':
    assert std_reduce == my_reduce(lst)