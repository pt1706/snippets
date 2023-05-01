from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    d = {}
    while nums:
        item = nums.pop()
        if d.get(item):
            return True
        d[item] = 1
    return False


def containsDuplicate_nlogn(nums: List[int]) -> bool:
    nums = sorted(nums)
    while len(nums) >= 2:
        num = nums.pop(0)
        if num == nums[0]:
            return True
    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    assert True is containsDuplicate(nums), '1 test'

    nums = [1, 2, 3, 4]
    assert False is containsDuplicate(nums), '2 test'

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert True is containsDuplicate(nums), '3 test'