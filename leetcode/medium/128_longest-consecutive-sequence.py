from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0
    num_set = set(nums)
    res = 0
    for n in nums:
        if n - 1 not in num_set:
            l = 1
            while n + l in num_set:
                l += 1
            res = max(res, l)
    return res


if __name__ == '__main__':
    nums = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
    assert 7 == longestConsecutive(nums)
