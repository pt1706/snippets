from typing import List


def longestSubarray(nums: List[int]) -> int:
    l = 0
    z = -1
    res = 0
    for r in range(len(nums)):
        if nums[r] == 0 and z == -1:
            z = r
        elif nums[r] == 0:
            l = z + 1
            z = r
        res = max(res, r - l)
    return res


if __name__ == '__main__':
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    assert 5 == longestSubarray(nums), 'test 1'

    nums = [1, 0, 0, 0, 0]
    assert 1 == longestSubarray(nums), 'test 2'
