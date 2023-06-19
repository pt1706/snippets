from typing import List


def equalPairs(grid: List[List[int]]) -> int:
    t_grid = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    for r in range(len(grid)):
        for c in range(len(grid)):
            t_grid[c][r] = grid[r][c]

    res = 0
    for r in grid:
        for c in t_grid:
            if r == c:
                res += 1
    return res


if __name__ == '__main__':
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    assert 1 == equalPairs(grid), 'test 1'

    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    assert 3 == equalPairs(grid), 'test 2'