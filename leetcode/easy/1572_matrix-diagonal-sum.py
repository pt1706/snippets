from typing import List


def diagonalSum(mat: List[List[int]]) -> int:
    res, n = 0, len(mat)
    for i in range(n):
        res += mat[i][i]
        res += mat[i][n - 1 - i]
    return res - (mat[n // 2][n // 2] if n % 2 != 0 else 0)


def diagonalSum_simple(mat: List[List[int]]) -> int:
    res = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i + j == len(mat) - 1 or i == j:
                res += mat[i][j]
    return res


if __name__ == '__main__':
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert 25 == diagonalSum(mat), 'test 1'

    mat = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    assert 8 == diagonalSum(mat), 'test 2'

    mat = [
        [11, 12, 13, 14],
        [21, 22, 23, 24],
        [31, 32, 33, 34],
        [41, 42, 43, 44]
    ]
    assert 220 == diagonalSum(mat), 'test 3'