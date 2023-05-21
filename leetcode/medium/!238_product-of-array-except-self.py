from functools import reduce
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    pre = [1 for _ in range(len(nums) + 2)]
    post = [1 for _ in range(len(nums) + 2)]
    for i in range(len(nums)):
        pre[i + 1] = pre[i] * nums[i]
    for i in range(len(nums) - 1, -1, -1):
        post[i + 1] = post[i + 2] * nums[i]

    res = []
    for i in range(len(nums)):
        item = pre[i] * post[i + 2]
        res.append(item)
    return res


def productExceptSelf_stupid(nums: List[int]) -> List[int]:
    p = reduce(lambda x, y: x * y, nums)
    res = []
    for i in range(len(nums)):
        if nums[i] != 0:
            res.append(int(p / nums[i]))
        else:
            res.append(reduce(lambda x, y: x * y, nums[:i] + nums[i + 1:]))
    return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    res = [24, 12, 8, 6]
    assert res == productExceptSelf(nums), 'test 1'

    nums = [-1, 1, 0, -3, 3]
    res = [0, 0, 9, 0, 0]
    assert res == productExceptSelf(nums), 'test 2'
