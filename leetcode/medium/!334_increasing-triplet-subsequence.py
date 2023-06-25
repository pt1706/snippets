from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    mn_1 = float('inf')
    mn_2 = float('inf')
    for i in nums:
        if i > mn_1:
            if i > mn_2:
                return True
            else:
                mn_2 = i
        else:
            mn_1 = i
    return False


def increasingTriplet_recurcive(nums: List[int]) -> bool:
    """time limit"""
    def dfs(i, c):
        if c >= 3:
            return True
        res = []
        for j in range(i, len(nums)):
            if nums[j] > nums[i]:
                res.append(dfs(j, c + 1))
        return any(res)

    res = []
    for i in range(len(nums)):
        res.append(dfs(i, 1))
    return any(res)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    assert True is increasingTriplet(nums), 'test 1'

    nums = [5, 4, 3, 2, 1]
    assert False is increasingTriplet(nums), 'test 2'

    nums = [2, 1, 5, 0, 4, 6]
    assert True is increasingTriplet(nums), 'test 3'

    nums = [0, 4, 2, 1, 0, -1, -3]
    assert False is increasingTriplet(nums), 'test 4'

    nums = [20, 100, 10, 12, 5, 13]
    assert True is increasingTriplet(nums), 'test 5'

    nums = [1, 5, 0, 4, 1, 3]
    assert True is increasingTriplet(nums), 'test 6'

    nums = [1, 1, 1, 1, 1, 1]
    assert False is increasingTriplet(nums), 'test 7'
