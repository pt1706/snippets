from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    i, j = 0, 0
    n = len(matrix)
    m = len(matrix[0])
    size = n * m
    res = []
    circle = 1
    while len(res) != size:
        res.append(matrix[i][j])
        if j < m - 1:
            j += 1
        elif i < n - 1:
            i += 1
        elif j > circle - 1:
            j -= 1
            m -= 1
        elif i != circle:
            i -= 1
            n -= 1
        else:
            n = len(matrix) - circle
            m = len(matrix[0]) - circle
            i, j = circle, circle
            circle += 1
    return res


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert res == spiralOrder(matrix), 'test 1'

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    res = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert res == spiralOrder(matrix), 'test 1'
