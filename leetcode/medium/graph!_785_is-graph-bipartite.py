from typing import List


def isBipartite(graph: List[List[int]]) -> bool:
    odd = [0 for _ in graph]

    def bfs(i):
        if odd[i]:
            return True
        odd[i] = -1
        q = [i]
        while q:
            i = q.pop(0)
            for n in graph[i]:
                if odd[n] == odd[i]:
                    return False
                elif not odd[n]:
                    q.append(n)
                    odd[n] = odd[i] * -1
        return True

    for i in range(len(graph)):
        if not bfs(i):
            return False

    return True


def isBipartite_my_try(graph: List[List[int]]) -> bool:
    """don't work"""
    red, green = [0], [i for i in graph[0]]
    f = True
    while f:
        f = False
        for i in range(1, len(graph)):
            edges = graph[i]
            if i in red:
                for ed in edges:
                    if ed in red:
                        return False
                    else:
                        green.append(ed)
            elif i in green:
                for ed in edges:
                    if ed in green:
                        return False
                    else:
                        red.append(ed)
            else:
                f = True
    return True


if __name__ == '__main__':
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    assert False is isBipartite(graph), 'test 1'

    graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    assert True is isBipartite(graph), 'test 2'

    graph = [[1], [0, 3], [3], [1, 2]]
    assert True is isBipartite(graph), 'test 3'

    graph = [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]]
    assert False is isBipartite(graph), 'test 4'