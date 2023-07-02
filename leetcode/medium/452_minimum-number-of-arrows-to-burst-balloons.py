from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
    points.sort()
    prev = points[0][1]
    res = 1
    for s, e in points[1:]:
        if s > prev:
            res += 1
            prev = e
        else:
            prev = min(prev, e)
    return res


if __name__ == '__main__':
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    assert 2 == findMinArrowShots(points), 'test 1'

    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert 4 == findMinArrowShots(points), 'test 2'

    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    assert 2 == findMinArrowShots(points), 'test 3'