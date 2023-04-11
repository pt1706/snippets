from typing import List


def majorityElement(nums: List[int]) -> int:
    res, maxCount = nums[0], 1
    for x in nums[1:]:
        if x == res:
            maxCount += 1
        elif maxCount == 0:
            res = x
            maxCount = 1
        else:
            maxCount -= 1
    return res


def majorityElement_extra_mem(nums: List[int]) -> int:
    count = {}
    res, maxCount = 0, 0
    for x in nums:
        count[x] = 1 + count.get(x, 0)
        res = x if maxCount <= count[x] else res
        maxCount = max(maxCount, count[x])
    return res


if __name__ == '__main__':
    nums = [10, 9, 9, 9, 10]
    assert 9 == majorityElement(nums), 'test 1'

    nums = [1, 3, 1, 1, 4, 1, 1, 5, 1, 1, 6, 2, 2]
    assert 1 == majorityElement(nums), 'test 2'

    nums = [3, 2, 3]
    assert 3 == majorityElement(nums), 'test 3'

    nums = [6, 5, 5]
    assert 5 == majorityElement(nums), 'test 4'

    nums = [2, 2, 1, 1, 1, 2, 2]
    assert 2 == majorityElement(nums), 'test 5'
