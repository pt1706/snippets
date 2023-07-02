from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    res_mx = res = sum(nums[:k])
    for i in range(k, len(nums)):
        res = res + (nums[i] - nums[i - k])
        res_mx = max(res_mx, res)
    return round(res_mx / k, 5)


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    assert 12.75000 == findMaxAverage(nums, k), 'test 1'

    nums = [0, 4, 0, 3, 2]
    k = 1
    assert 4.00000 == findMaxAverage(nums, k), 'test 2'