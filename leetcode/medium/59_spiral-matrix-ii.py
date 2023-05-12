from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    i, j = 0, 0
    c = 1
    el = 1
    max_n = n
    res = [[0 for _ in range(n)] for _ in range(n)]
    while el <= max_n * max_n:
        res[i][j] = el
        el += 1
        if j < n - 1:
            j += 1
        elif i < n - 1:
            i += 1
        elif j >= n - 1 and j > c - 1:
            n -= 1
            j -= 1
        elif i >= n - 1 and i > c:
            i -= 1
        else:
            n = max_n - c
            i, j = c, c
            c += 1
    return res


if __name__ == '__main__':
    n = 5
    res = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
    ]
    assert res == generateMatrix(n), 'test 1'
