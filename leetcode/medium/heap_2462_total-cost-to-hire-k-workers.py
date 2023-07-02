from collections import deque
from heapq import heappop, heapify, heappush
from typing import List


def totalCost(costs: List[int], k: int, candidates: int) -> int:
    res = 0
    l_h = costs[:candidates]
    costs = costs[candidates:]
    r_h = costs[-candidates:]
    h = costs[: -candidates]
    heapify(l_h)
    heapify(r_h)
    h = deque(h)
    while k and (l_h or r_h):
        k -= 1
        if l_h:
            l = heappop(l_h)
        else:
            l = float('inf')
        if r_h:
            r = heappop(r_h)
        else:
            r = float('inf')

        if l == r or r > l:
            heappush(r_h, r)
            res += l
            if h:
                new = h.popleft()
                heappush(l_h, new)

        else:
            heappush(l_h, l)
            res += r
            if h:
                new = h.pop()
                heappush(r_h, new)
    return res


if __name__ == '__main__':
    costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
    k = 3
    candidates = 4
    assert 11 == totalCost(costs, k, candidates), 'test 1'

    costs = [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58]
    k = 11
    candidates = 2
    assert 423 == totalCost(costs, k, candidates), 'test 2'

    costs = [18, 64, 12, 21, 21, 78, 36, 58, 88, 58, 99, 26, 92, 91, 53, 10,
             24, 25, 20, 92, 73, 63, 51, 65, 87, 6, 17, 32, 14, 42, 46, 65,
             43, 9, 75]
    k = 13
    candidates = 23
    assert 223 == totalCost(costs, k, candidates), 'test 3'

    costs = [57, 33, 26, 76, 14, 67, 24, 90, 72, 37, 30]
    k = 11
    candidates = 2
    assert 526 == totalCost(costs, k, candidates), 'test 4'
