from typing import List


def arraySign(nums: List[int]) -> int:
    res = 1
    for x in nums:
        if x == 0:
            return 0
        elif x < 0:
            res *= -1
    return res


if __name__ == '__main__':
    nums = [-1, -2, -3, -4, 3, 2, 1]
    assert 1 == arraySign(nums), 'test 1'

    nums = [1, 5, 0, 2, -3]
    assert 0 == arraySign(nums), 'test 2'

    nums = [-1, 1, -1, 1, -1]
    assert -1 == arraySign(nums), 'test 3'