from collections import deque
from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:
    """dfs"""
    def dfs(i):
        v.add(i)
        for j in range(n):
            if j not in v and isConnected[i][j] == 1:
                dfs(j)
    res = 0
    v = set()
    n = len(isConnected)
    for i in range(n):
        if i not in v:
            res += 1
            dfs(i)

    return res


def findCircleNum_bfs(isConnected: List[List[int]]) -> int:
    res = 0
    v = set()
    q = deque()
    n = len(isConnected)
    for i in range(n):
        if i not in v:
            q.append(i)
            while q:
                k = q.popleft()
                v.add(k)
                item = isConnected[k]
                for j in range(n):
                    if j != i and j not in v and item[j] == 1:
                        q.append(j)
            res += 1
    return res


if __name__ == '__main__':
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    assert 2 == findCircleNum(isConnected), 'test 1'

    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert 3 == findCircleNum(isConnected), 'test 2'

    isConnected = [[1]]
    assert 1 == findCircleNum(isConnected), 'test 3'