from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(node, d='r'):
        nonlocal res
        if not node:
            return 0
        if not node.left and not node.right and d == 'l':
            res += node.val
        dfs(node.left, 'l')
        dfs(node.right)

    dfs(root)
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
    assert 24 == sumOfLeftLeaves(root), 'test 1'

    root = TreeNode(1)
    assert 0 == sumOfLeftLeaves(root), 'test 2'

