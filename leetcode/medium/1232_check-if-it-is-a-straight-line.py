from typing import List


def checkStraightLine(coordinates: List[List[int]]) -> bool:
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    for x, y in coordinates[2:]:
        if (y2 - y) * (x1 - x) != (y1 - y) * (x2 - x):
            return False
    return True


def checkStraightLine_long(coordinates: List[List[int]]) -> bool:

    if len(coordinates) == 2:
        return True

    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    if x1 - x2 == 0:
        for x, y in coordinates[2:]:
            if x != x1:
                return False
        return True

    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1

    for x, y in coordinates[2:]:
        if x * a + b != y:
            return False
    return True


if __name__ == '__main__':
    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    assert True is checkStraightLine(coordinates), 'test 1'

    coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    assert False is checkStraightLine(coordinates), 'test 2'