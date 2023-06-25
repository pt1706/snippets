from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1


def moveZeroes_my(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return
    l = 0
    r = 1
    while l < len(nums) - 1 and r < len(nums):
        if nums[l] == 0:
            while r < len(nums) and nums[r] == 0:
                r += 1
            if r > len(nums) - 1:
                return
            nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r += 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    assert [1, 3, 12, 0, 0] == nums, 'test 1'

