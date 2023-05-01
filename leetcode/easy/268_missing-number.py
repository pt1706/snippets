from typing import List


def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    res = 0
    for i in nums:
        res += n - i
        n -= 1
    return res


def missingNumber_stupid(nums: List[int]) -> int:
    return (set(range(len(nums) + 1)) - set(nums)).pop()


if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    assert 8 == missingNumber(nums), 'test 1'

    nums = [3, 0, 1]
    assert 2 == missingNumber(nums), 'test 2'

    nums = [0, 1]
    assert 2 == missingNumber(nums), 'test 3'

