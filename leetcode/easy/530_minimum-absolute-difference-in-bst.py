from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def getMinimumDifference(root: Optional[TreeNode]) -> int:
    res = float('inf')

    def dfs(node):
        nonlocal res
        if not node:
            return None
        if node.left:
            res = min(res, node.val - node.left.val)
            cur = node.left
            while cur.right:
                res = min(res, node.val - cur.right.val)
                cur = cur.right

        if node.right:
            res = min(res, node.right.val - node.val)
            cur = node.right
            while cur.left:
                res = min(res, cur.left.val - node.val)
                cur = cur.left
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return res


def getMinimumDifference_stupid(root: Optional[TreeNode]) -> int:
    """time limit"""
    res = float('inf')

    def dfs(val, node):
        nonlocal res
        if not node:
            return None
        if (val, node.val) in d:
            return None
        res = min(res, abs(abs(val) - abs(node.val)))
        dfs(val, node.left)
        dfs(val, node.right)
        dfs(node.val, node.left)
        dfs(node.val, node.right)
    dfs(res, root)
    return res


def getMinimumDifference_simple(root: Optional[TreeNode]) -> int:
    def dfs(node):
        if not node or (not node.left and not node.right):
            return float('inf')
        if node.left and node.right:
            mn_l = node.val - node.left.val
            mn_r = node.right.val - node.val
        elif not node.right:
            mn_l = node.val - node.left.val
            mn_r = float('inf')
        else:
            mn_r = node.right.val - node.val
            mn_l = float('inf')

        return min(mn_r, mn_l, dfs(node.left), dfs(node.right))

    return dfs(root)


if __name__ == '__main__':
    root = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(6)
    )
    k = 1
    assert 1 == getMinimumDifference(root), 'test 1'

    root = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(6)
    )
    k = 1
    assert 1 == getMinimumDifference(root), 'test 1'

    root = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(6)
    )
    assert 1 == getMinimumDifference(root), 'test 1'

    root = TreeNode(
        5,
        TreeNode(
            4
        ),
        TreeNode(7)
    )
    assert 1 == getMinimumDifference(root), 'test 2'