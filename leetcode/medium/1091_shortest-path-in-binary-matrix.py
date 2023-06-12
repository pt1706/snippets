from collections import deque
from typing import List


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    if grid[0][0] != 0:
        return -1
    n = len(grid) - 1
    v = {(0, 0): 1}
    q = deque()
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        s = v[(r, c)]
        steps = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        for s_r, s_c in steps:
            i = r + s_r
            j = c + s_c
            if 0 <= i <= n and 0 <= j <= n and grid[i][j] == 0:
                if (i, j) not in v or v[(i, j)] > s + 1:
                    q.append((i, j))
                    v[(i, j)] = s + 1
    return v[(n, n)] if (n, n) in v else -1


if __name__ == '__main__':
    grid = [[0, 1], [1, 0]]
    assert 2 == shortestPathBinaryMatrix(grid), 'test 1'

    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    assert 4 == shortestPathBinaryMatrix(grid), 'test 2'

    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    assert -1 == shortestPathBinaryMatrix(grid), 'test 3'
