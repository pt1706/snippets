from typing import List


def removeElement(nums: List[int], val: int) -> int:
    l = 0
    for r in range(len(nums)):
        if nums[r] == val:
            continue
        else:
            nums[l] = nums[r]
            l += 1
    return l


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    assert 2 == removeElement(nums, 3)
    assert nums == [2, 2, 2, 3]
