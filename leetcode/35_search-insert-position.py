from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while True:
        mid = low + (high - low) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid
        else:
            high = mid
        if high - low <= 1:
            if target > nums[high]:
                return high + 1
            elif target == nums[high]:
                return high
            elif target <= nums[low]:
                return low
            return high


if __name__ == '__main__':
    nums = [1]
    target = 0
    assert 0 == searchInsert(nums, target)

    nums = [1, 3, 5]
    target = 1
    assert 0 == searchInsert(nums, target)

    nums = [1, 3, 5, 6]
    target = 7
    assert 4 == searchInsert(nums, target)

    nums = [1, 3, 5, 6, 8, 9]
    target = 7
    assert 4 == searchInsert(nums, target)

    nums = [1, 3, 5, 6]
    target = 5
    assert 2 == searchInsert(nums, target)

    nums = [1, 3, 5, 6]
    target = 2
    assert 1 == searchInsert(nums, target)
