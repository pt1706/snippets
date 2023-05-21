class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        res = []
        for n in self.neighbors:
            res.append(n.val)
        return str(res)


def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return None
    d = {}

    def dfs(node):
        if node in d:
            return d[node]
        copy = Node(node.val)
        d[node] = copy
        for n in node.neighbors:
            copy.neighbors.append(dfs(n))
        return copy

    return dfs(node)


if __name__ == '__main__':
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_1.neighbors.append(node_2)
    node_1.neighbors.append(node_4)
    node_2.neighbors.append(node_1)
    node_2.neighbors.append(node_3)
    node_3.neighbors.append(node_2)
    node_3.neighbors.append(node_4)
    node_4.neighbors.append(node_1)
    node_4.neighbors.append(node_3)
    print(cloneGraph(node_1))