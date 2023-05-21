from typing import List


def maxScore(nums: List[int]) -> int:
    res = []
    while nums:
        if nums[0] == 1 and len(nums) > 2:
            item = nums.pop(1)
        elif nums[0] == 1:
            res = [1] + res
            nums = []
        else:
            item = nums.pop(0)
        for i in range(len(nums)):
            if nums[i] / item == 2:
                nums.pop(i)
                res.append(item)
                break
    result = 0
    for i in range(1, len(res) + 1):
        result += i * res[i - 1]
    return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    assert 14 == maxScore(nums), 'test 1'

    nums = [3, 4, 6, 8]
    assert 11 == maxScore(nums), 'test 2'

    nums = [1, 2]
    assert 1 == maxScore(nums), 'test 3'