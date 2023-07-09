from typing import List


def findPeakElement(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (r - l) // 2 + l
        if m < len(nums) - 1 and nums[m] < nums[m + 1]:
            l = m + 1
        elif m >= 0 and nums[m] < nums[m - 1]:
            r = m - 1
        else:
            return m


if __name__ == '__main__':
    nums = [1, 2, 3]
    assert 2 == findPeakElement(nums), 'test 1'

    nums = [1, 2, 1]
    assert 1 == findPeakElement(nums), 'test 2'
