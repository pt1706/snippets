def uniquePaths(m: int, n: int) -> int:
    if n == 1 or m == 1:
        return 1
    mt = [[1 for _ in range(n)] for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            mt[r][c] = max(mt[r][c], mt[r - 1][c] + mt[r][c - 1])
    return mt[m - 1][n - 1]


if __name__ == '__main__':
    m = 3
    n = 7
    assert 28 == uniquePaths(m, n), 'test 1'

    m = 1
    n = 7
    assert 1 == uniquePaths(m, n), 'test 2'

    m = 3
    n = 2
    assert 3 == uniquePaths(m, n), 'test 3'