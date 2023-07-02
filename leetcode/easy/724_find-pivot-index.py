from typing import List


def pivotIndex(nums: List[int]) -> int:
    sm = sum(nums)
    left = 0
    for i in range(len(nums)):
        pivot = nums[i]
        sm -= pivot
        if left == sm:
            return i
        left += pivot
    return - 1


if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    assert 3 == pivotIndex(nums), 'test 1'

    nums = [1, 2, 3]
    assert -1 == pivotIndex(nums), 'test 2'

    nums = [2, 1, -1]
    assert 0 == pivotIndex(nums), 'test 3'