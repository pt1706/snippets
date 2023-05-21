from typing import List


def maxArea(height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    res = min(height[l], height[r]) * (r - l)

    while l != r:
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        res = max(res, min(height[l], height[r]) * (r - l))

    return res


def maxArea_simple(height: List[int]) -> int:
    l = 0
    res = 0

    while l < len(height):
        r = l + 1
        while r < len(height):
            if min(height[l], height[r]) * (r - l) > res:
                res = min(height[l], height[r]) * (r - l)
            r += 1
        l += 1
        while l < len(height) and height[l] < height[l - 1]:
            l += 1
    return res


if __name__ == '__main__':
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert 49 == maxArea(nums), 'test 1'

    nums = [1, 2, 4, 3]
    assert 4 == maxArea(nums), 'test 2'

    nums = [1, 2, 1]
    assert 2 == maxArea(nums), 'test 3'

    nums = [1, 8, 6, 2, 5, 4, 8, 25, 7]
    assert 49 == maxArea(nums), 'test 4'

    nums = [2, 3, 4, 5, 18, 17, 6]
    assert 17 == maxArea(nums), 'test 5'