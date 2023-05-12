from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    res = [[]]

    def dfs(node, level):
        nonlocal res
        if not node:
            return 0
        if level >= len(res):
            res.append([node.val])
        else:
            res[level].append(node.val)

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
        return 0
    dfs(root, 0)
    return res


def levelOrder_iter(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    res = [[root.val]]
    q = [root]
    while q:
        level = []
        nq = []
        while q:
            item = q.pop(0)
            if item.left:
                nq.append(item.left)
                level.append(item.left.val)
            if item.right:
                nq.append(item.right)
                level.append(item.right.val)
        if level:
            res.append(level)
        q = nq
    return res


if __name__ == '__main__':
    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7)
        )
    )
    res = [[3], [9, 20], [15, 7]]
    assert res == levelOrder(root), 'test 1'

    root = TreeNode(1)
    res = [[1]]
    assert res == levelOrder(root), 'test 2'