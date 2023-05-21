from typing import List


def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    def bfs(r, c):
        q = [(r, c)]
        while q:
            r, c = q.pop()
            for r, c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (r >= 0 and r < row) and (c >= 0 and c < col) and (r, c) not in visited and grid[r][c] == '1':
                    q.append((r, c))
                    visited.append((r, c))

    island = 0
    visited = []
    row, col = len(grid), len(grid[0])
    for r in range(row):
        for c in range(col):
            if grid[r][c] == '1' and (r, c) not in visited:
                island += 1
                visited.append((r, c))
                bfs(r, c)
    return island


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert 1 == numIslands(grid), 'test 1'

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert 3 == numIslands(grid), 'test 2'

    grid = [
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]
    ]
    assert 1 == numIslands(grid), 'test 2'
