import heapq
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-x for x in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        x = heapq.heappop(stones)
        y = heapq.heappop(stones)
        if y != x:
            heapq.heappush(stones, x - y)
    stones.append(0)
    return abs(stones[0])


def lastStoneWeight_stupid(stones: List[int]) -> int:
    stones = sorted(stones, reverse=True)
    while len(stones) >= 2:
        stones = sorted(stones, reverse=True)
        y, x = stones[0:2]
        if y == x:
            stones = stones[2:]
        else:
            stones = [y - x] + stones[2:]
    if len(stones) == 1:
        x, = stones
        return x
    else:
        return 0


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    assert 1 == lastStoneWeight(stones), 'test 1'

    stones = [1]
    assert 1 == lastStoneWeight(stones), 'test 2'