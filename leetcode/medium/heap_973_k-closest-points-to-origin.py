import heapq
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    res = []
    for p in points:
        d = (p[0] ** 2 + p[1] ** 2) ** .5
        heap.append([d, p[0], p[1]])
    heapq.heapify(heap)
    while k:
        d, x, y = heapq.heappop(heap)
        res.append([x, y])
        k -= 1
    return res


if __name__ == '__main__':
    points = [[1, 3], [-2, 2]]
    k = 1
    assert [[-2, 2]] == kClosest(points, k)
