from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    res = 0
    l = 0
    for r in range(len(nums)):
        if nums[r] == 0 and k > 0:
            k -= 1
        elif nums[r] == 0 and k == 0:
            while nums[l] == 1:
                l += 1
            l += 1
        res = max(r - l + 1, res)
    return res


def longestOnes_my(nums: List[int], k: int) -> int:
    """time limit"""
    res = 0
    for i in range(len(nums)):
        k_i = k
        res_i = 0
        for j in range(i, len(nums)):
            if nums[j] == 0 and k_i == 0:
                break
            if nums[j] == 0 and k_i > 0:
                k_i -= 1
            res_i += 1
            res = max(res, res_i)
    return res


def longestOnes_recursive(nums: List[int], k: int) -> int:
    """time limit"""
    def dfs(limit, k):
        l, r = limit
        if r >= len(nums):
            return r - l
        if nums[r] == 0 and k == 0:
            return max(r - l, dfs((r + 1, r + 1), k))
        if nums[r] == 1:
            return dfs((l, r + 1), k)
        return max(dfs((l, r + 1), k - 1), dfs((r + 1, r + 1), k))
    return dfs((0, 0), k)


if __name__ == '__main__':
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    assert 6 == longestOnes(nums, k), 'test 1'

    nums = [0, 0, 1, 1, 1, 0, 0]
    k = 0
    assert 3 == longestOnes(nums, k), 'test 2'