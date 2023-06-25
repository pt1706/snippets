import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    mx = max(piles)
    mn = 1
    res = mx

    while mn <= mx:
        mid = (mx + mn) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)

        if hours <= h:
            res = min(res, mid)
            mx = mid - 1
        else:
            mn = mid + 1
    return res


if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    h = 8
    assert 4 == minEatingSpeed(piles, h), 'test 1'

    piles = [30, 11, 23, 4, 20]
    h = 5
    assert 30 == minEatingSpeed(piles, h), 'test 2'

    piles = [30, 11, 23, 4, 20]
    h = 6
    assert 23 == minEatingSpeed(piles, h), 'test 3'

    piles = [312884470]
    h = 312884469
    assert 2 == minEatingSpeed(piles, h), 'test 4'