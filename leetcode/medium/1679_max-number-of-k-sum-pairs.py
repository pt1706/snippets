from typing import List


def maxOperations(nums: List[int], k: int) -> int:
    nums.sort()
    l = 0
    r = len(nums) - 1
    res = 0
    while l < r:
        if nums[l] + nums[r] == k:
            l += 1
            r -= 1
            res += 1
        if nums[l] + nums[r] > k:
            r -= 1
        if nums[l] + nums[r] < k:
            l += 1
    return res


def maxOperations_simple(nums: List[int], k: int) -> int:
    v = []
    res = 0
    for i in range(len(nums)):
        if i not in v:
            for j in range(len(nums)):
                if i != j and j not in v and nums[i] + nums[j] == k:
                    res += 1
                    v.append(i)
                    v.append(j)
                    break
    return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    k = 5
    assert 2 == maxOperations(nums, k), 'test 1'

    nums = [3, 1, 3, 4, 3]
    k = 6
    print(maxOperations(nums, k))
    assert 1 == maxOperations(nums, k), 'test 2'

