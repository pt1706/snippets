from math import floor


def bulbSwitch(n: int) -> int:
    return floor(n ** .5)


if __name__ == '__main__':
    n = 3
    assert 1 == bulbSwitch(n), 'test 1'

    n = 0
    assert 0 == bulbSwitch(n), 'test 2'

    n = 1
    assert 1 == bulbSwitch(n), 'test 3'

    n = 17
    assert 4 == bulbSwitch(n), 'test 4'
