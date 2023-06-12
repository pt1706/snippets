from typing import List


def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        m = (r + l) // 2
        if nums[m + 1] < nums[m]:
            return nums[m + 1]
        if nums[l] < nums[m]:
            l = m
        else:
            r = m
    return nums[0]


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    assert 1 == findMin(nums), 'test 1'

    nums = [4, 5, 6, 7, 0, 1, 2]
    assert 0 == findMin(nums), 'test 2'

    nums = [11, 13, 15, 17]
    assert 11 == findMin(nums), 'test 3'

    nums = [3, 1, 2]
    assert 1 == findMin(nums), 'test 4'

    nums = [5, 1, 2, 3, 4]
    assert 1 == findMin(nums), 'test 5'