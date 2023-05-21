from typing import List


def findSmallestSetOfVertices(n: int, edges: List[List[int]]) -> List[int]:
    def dfs(n, v, res):
        if not n:
            return res
        if not v:
            item = n.pop()
            if item[1] not in res:
                v.append(item[1])
            new_n = []
            while n:
                node = n.pop()
                if item[0] == node[0]:
                    if node[1] not in res:
                        v.append(node[1])
                else:
                    new_n.append(node)
            res.append(item[0])
            return dfs(new_n, v, res)
        else:
            item = v.pop()
            new_n = []
            while n:
                node = n.pop()
                if item == node[0]:
                    if node[1] not in res:
                        v.append(node[1])
                else:
                    new_n.append(node)
            res.append(item)
            return dfs(new_n, v, res)
        res = [[] for _ in range(n)]
        for edge in range(len(edges)):
            res = min(res, dfs())
        return