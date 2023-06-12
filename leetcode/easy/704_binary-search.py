from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while r >= l:
        m = (r + l) // 2
        if nums[m] == target:
            return m
        if nums[m] > target:
            r = m - 1
        if nums[m] < target:
            l = m + 1
    return -1


def search_my(nums: List[int], target: int) -> int:
    def bsr(l, r):
        if r - l <= 1:
            return r if nums[r] == target else l if nums[l] == target else -1
        p_i = (r + l) // 2
        if nums[p_i] == target:
            return p_i
        elif nums[p_i] > target:
            r = p_i
            return bsr(l, r)
        else:
            l = p_i
            return bsr(l, r)

    return bsr(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert 4 == search(nums, target), 'test 1'

    nums = [5]
    target = 5
    assert 0 == search(nums, target), 'test 2'