from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            sub_res = nums[i] + nums[r] + nums[l]
            if sub_res > 0:
                r -= 1
            elif sub_res < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res


def threeSum_simple(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l != r:
            if nums[i] + nums[r] + nums[l] == 0 and sorted([nums[i], nums[r], nums[l]]) not in res:
                res.append(sorted([nums[i], nums[r], nums[l]]))
            if nums[i] + nums[r] + nums[l] < 0:
                l += 1
            else:
                r -= 1
    return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    assert [[-1, -1, 2], [-1, 0, 1]] == threeSum(nums), 'test 1'
