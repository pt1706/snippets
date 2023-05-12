import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    def quik_sort(nums, k):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return [nums[1], nums[0]][k - 1] if nums[0] <= nums[1] else [nums[0], nums[1]][k - 1]
        pivot = nums[0]
        l = []
        g = []
        for i in nums[1:]:
            if i <= pivot:
                l.append(i)
            else:
                g.append(i)
        if len(g) == k - 1:
            return pivot
        if len(g) > k - 1:
            return quik_sort(g, k)
        if len(g) < k - 1:
            return quik_sort(l, k - len(g) - 1)
    res = quik_sort(nums, k)
    return res


def findKthLargest_quick_sort(nums: List[int], k: int) -> int:
    def quik_sort(nums):
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            return [nums[0], nums[1]] if nums[0] <= nums[1] else [nums[1], nums[0]]
        pivot = nums[0]
        l = []
        g = []
        for i in nums[1:]:
            if i <= pivot:
                l.append(i)
            else:
                g.append(i)
        return quik_sort(l) + [pivot] + quik_sort(g)
    res = quik_sort(nums)
    return res[-k]


def findKthLargest_naive(nums: List[int], k: int) -> int:
    nums = [-x for x in nums]
    heapq.heapify(nums)
    res = 0
    while k:
        res = heapq.heappop(nums)
        k -= 1
    return -res


def findKthLargest_super_naive(nums: List[int], k: int) -> int:
    nums.sort()
    return nums[-k]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    # print(findKthLargest(nums, k))
    assert 5 == findKthLargest(nums, k), 'test 1'

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    assert 4 == findKthLargest(nums, k), 'test 2'

    nums = [2, 1]
    k = 1
    assert 2 == findKthLargest(nums, k), 'test 3'

    nums = [7, 6, 5, 4, 3, 2, 1]
    k = 2
    assert 6 == findKthLargest(nums, k), 'test 4'
