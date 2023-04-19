from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    d = {}
    for i in range(len(nums)):
        item = nums[i]
        if d.get(item, None) is not None:
            if abs(i - d[item]) <= k:
                return True
        d[item] = i
    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    k = 3
    assert True is containsNearbyDuplicate(nums, k), '1 test'
