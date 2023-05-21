from typing import List


def shortestBridge(grid: List[List[int]]) -> int:
    def bfs(i, j, island):
        q = [(i, j)]
        while q:
            i, j = q.pop(0)
            for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= r < n and 0 <= c < n and grid[r][c] == 1 and (r, c) not in island:
                    island.add((r, c))
                    q.append((r, c))

    i_1 = set()
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and (i, j) not in i_1 and (i, j):
                i_1.add((i, j))
                bfs(i, j, i_1)
                res = 0
                while True:
                    res += 1
                    tmp = set()
                    for i, j in i_1:
                        for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                            if 0 <= r < n and 0 <= c < n and (r, c) not in i_1 and grid[r][c] == 0:
                                tmp.add((r, c))
                            if 0 <= r < n and 0 <= c < n and (r, c) not in i_1 and grid[r][c] == 1:
                                return res - 1
                    i_1.update(tmp)


def shortestBridge_my(grid: List[List[int]]) -> int:
    def bfs(i, j, island):
        q = [(i, j)]
        while q:
            i, j = q.pop(0)
            for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= r < n and 0 <= c < n and grid[r][c] == 1 and (r, c) not in island:
                    island.add((r, c))
                    q.append((r, c))

    i_1 = set()
    i_2 = set()
    n = len(grid)
    f = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1 and (i, j) not in i_1 and (i, j) not in i_2:
                if not f:
                    i_1.add((i, j))
                    bfs(i, j, i_1)
                    f = 1
                else:
                    i_2.add((i, j))
                    bfs(i, j, i_2)
    res = 0
    while True:
        res += 1
        tmp = set()
        for i, j in i_1:
            for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= r < n and 0 <= c < n and (r, c) not in i_1:
                    tmp.add((r, c))
        i_1.update(tmp)
        if i_1 & i_2:
            return res - 1


if __name__ == '__main__':
    grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    assert 2 == shortestBridge(grid), 'test 1'

    grid = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    assert 1 == shortestBridge(grid), 'test 2'