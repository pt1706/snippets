from typing import List


def largestAltitude(gain: List[int]) -> int:
    res = 0
    hight = 0
    for i in gain:
        hight += i
        res = max(res, hight)
    return res


if __name__ == '__main__':
    gain = [-5, 1, 5, 0, -7]
    assert 1 == largestAltitude(gain), 'test 1'

    gain = [-4, -3, -2, -1, 4, 3, 2]
    assert 0 == largestAltitude(gain), 'test 1'
