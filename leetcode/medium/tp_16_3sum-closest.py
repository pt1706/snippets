from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    res = 0
    dif = float('inf')
    nums.sort()
    for i in range(len(nums)):
        l, r = i + 1, len(nums) - 1
        while l < r:
            t = nums[i] + nums[l] + nums[r]
            if abs(target - t) < dif:
                dif = abs(target - t)
                res = t
            if t > target:
                r -= 1
            else:
                l += 1
    return res


def threeSumClosest_naive(nums: List[int], target: int) -> int:
    """timelimit"""
    res = 0
    dif = float('inf')
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                t = nums[i] + nums[j] + nums[k]
                if abs(t - target) < dif:
                    dif = abs(target - t)
                    res = t
    return res


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    assert 2 == threeSumClosest(nums, 1)
