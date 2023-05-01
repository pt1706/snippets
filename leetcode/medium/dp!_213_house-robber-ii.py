from typing import List


def rob(nums: List[int]) -> int:
    def max_rob(nums):
        r_1, r_2 = 0, 0
        for n in nums:
            tmp = r_2
            r_2 = max(r_1 + n, r_2)
            r_1 = tmp
        return r_2

    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    return max(max_rob(nums[:-1]), max_rob(nums[1:]))


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    assert 4 == rob(nums), 'test 1'

    nums = [1, 2, 3]
    assert 3 == rob(nums), 'test 2'
