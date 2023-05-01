from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    r, l = cost[0], cost[1]
    if len(cost) > 2:
        for i in cost[2:]:
            tmp = min(r, l) + i
            r = l
            l = tmp
    return min(r, l)


if __name__ == '__main__':
    cost = [10, 15, 20]
    assert 15 == minCostClimbingStairs(cost), 'test 1'

    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    assert 6 == minCostClimbingStairs(cost), 'test 2'
