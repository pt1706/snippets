from typing import List


def singleNumber(nums: List[int]) -> int:
    res = 0
    for x in nums:
        res = res ^ x
    return res


if __name__ == '__main__':
    nums = [2, 2, 1]
    assert 1 == singleNumber(nums)

    nums = [4, 1, 2, 1, 2]
    assert 4 == singleNumber(nums)

    nums = [1]
    assert 1 == singleNumber(nums)
