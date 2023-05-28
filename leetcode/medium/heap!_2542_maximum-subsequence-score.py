import heapq
from functools import reduce
from typing import List


def maxScore(nums1: List[int], nums2: List[int], k: int) -> int:
    """with min() worse runtime"""
    n = list(zip(nums1, nums2))
    n = sorted(n, key=lambda x: x[1], reverse=True)
    sum_n_1 = 0
    min_n_1 = []
    res = 0

    for n_1, n_2 in n:
        if len(min_n_1) == k:
            mn = min(min_n_1)
            sum_n_1 -= mn
            sum_n_1 += n_1
            min_n_1.remove(mn)
            min_n_1.append(n_1)
        else:
            sum_n_1 += n_1
            min_n_1.append(n_1)

        if len(min_n_1) == k:
            res = max(res, sum_n_1 * n_2)

    return res


def maxScore_heap(nums1: List[int], nums2: List[int], k: int) -> int:
    n = list(zip(nums1, nums2))
    n = sorted(n, key=lambda x: x[1], reverse=True)
    sum_n_1 = 0
    heap_n_1 = []
    res = 0

    for n_1, n_2 in n:
        if len(heap_n_1) == k:
            mn = heapq.heappop(heap_n_1)
            sum_n_1 -= mn
            sum_n_1 += n_1
            heapq.heappush(heap_n_1, n_1)
        else:
            sum_n_1 += n_1
            heapq.heappush(heap_n_1, n_1)

        if len(heap_n_1) == k:
            res = max(res, sum_n_1 * n_2)

    return res


def maxScore_my(nums1: List[int], nums2: List[int], k: int) -> int:
    """don't work with testcase 3"""
    def bfs(i, res):
        if i >= len(nums1) - 1:
            return reduce(lambda x, y: x + y, [nums1[j] for j in res]) * min([nums2[j] for j in res])
        if len(res) < k:
            res.append(i)
            return bfs(i + 1, res)
        max_res = res
        mx = reduce(lambda x, y: x + y, [nums1[j] for j in res]) * min([nums2[j] for j in res])
        for y in range(k):
            if nums2[res[y]] == 0:
                max_res = res[:y] + res[y + 1:] + [i]
                return bfs(i + 1, max_res)
            new_res = res[:y] + res[y + 1:] + [i]
            new_mx = reduce(lambda x, y: x + y, [nums1[j] for j in new_res]) * min([nums2[j] for j in new_res])
            if new_mx > mx:
                max_res = new_res
        return bfs(i + 1, max_res)
    return bfs(0, [])


if __name__ == '__main__':
    nums1 = [1, 3, 3, 2]
    nums2 = [2, 1, 3, 4]
    k = 3
    assert 12 == maxScore(nums1, nums2, k), 'test 1'

    nums1 = [79, 76, 41, 28, 41, 66, 44, 30, 25]
    nums2 = [25, 0, 69, 67, 55, 0, 9, 77, 26]
    k = 7
    assert 2592 == maxScore(nums1, nums2, k), 'test 2'

    nums1 = [88, 50, 63, 91, 70, 98, 45, 43, 1, 77]
    nums2 = [92, 69, 29, 83, 70, 38, 49, 2, 8, 62]
    k = 9
    assert 4664 == maxScore(nums1, nums2, k), 'test 3'

    nums1 = [2, 1, 14, 12]
    nums2 = [11, 7, 13, 6]
    k = 3
    assert 168 == maxScore(nums1, nums2, k), 'test 4'

