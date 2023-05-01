from typing import List


def rob(nums: List[int]) -> int:
    """
    DP solution
    """
    r_1, r_2 = 0, 0
    for n in nums:
        tmp = max(n + r_1, r_2)
        r_1 = r_2
        r_2 = tmp
    return r_2


def rob_rec_and_cash(nums: List[int]) -> int:
    d = {}

    def dfs(nums, res):
        if not nums:
            return res
        tmp = (tuple(nums), res)
        if not d.get(tmp):
            d[tmp] = max(dfs(nums[2:], res + nums[0]), dfs(nums[1:], res))
        return d[tmp]

    return dfs(nums, 0)


def rob_rec(nums: List[int]) -> int:
    def dfs(nums, res):
        if not nums:
            return res
        return max(dfs(nums[2:], res + nums[0]), dfs(nums[1:], res))
    return dfs(nums, 0)


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    assert 12 == rob(nums), 'test 1'

    nums = [
        183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234,
        100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81,
        185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247,
        211
    ]
    assert 3365 == rob(nums), 'test 2'