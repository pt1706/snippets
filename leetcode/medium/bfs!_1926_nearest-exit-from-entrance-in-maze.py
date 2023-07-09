from collections import deque
from typing import List


def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    maze[entrance[0]][entrance[1]] = '+'
    direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    q = deque()
    q.append([entrance[0], entrance[1], 0])

    while q:
        r, c, d = q.popleft()
        for dr, dc in direction:
            row = r + dr
            col = c + dc
            if 0 > row or row > len(maze) - 1 or 0 > col or col > len(maze[0]) - 1 or maze[row][col] == '+':
                continue
            if row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]) - 1:
                return d + 1
            maze[row][col] = '+'
            q.append([row, col, d + 1])
    return -1


def nearestExit_my(maze: List[List[str]], entrance: List[int]) -> int:
    v = [entrance]
    res = 0
    direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    q = [entrance]
    n_q = []
    while q or n_q:
        res += 1
        while q:
            cur = q.pop()
            for r, c in direction:
                row = cur[0] + r
                col = cur[1] + c
                if 0 > row or row > len(maze) - 1 or 0 > col or col > len(maze[0]) - 1 or maze[row][col] == '+':
                    continue
                if [row, col] not in v and (row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]) - 1):
                    return res
                if [row, col] not in v:
                    v.append([row, col])
                    n_q.append([row, col])
        q = n_q[:]
        n_q = []
    return -1


if __name__ == '__main__':
    maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    entrance = [1, 0]
    assert 2 == nearestExit(maze, entrance), 'test 1'

    maze = [["+", ".", "+", "+", "+", "+", "+"],
            ["+", ".", "+", ".", ".", ".", "+"],
            ["+", ".", "+", ".", "+", ".", "+"],
            ["+", ".", ".", ".", "+", ".", "+"],
            ["+", "+", "+", "+", "+", ".", "+"]]
    entrance = [0, 1]
    assert 12 == nearestExit(maze, entrance), 'test 2'
