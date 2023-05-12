from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def dfs(node, l, r):
        if not node:
            return True
        if node.val <= l or node.val >= r:
            return False
        return dfs(node.left, l, node.val) and dfs(node.right, node.val, r)
    return dfs(root, float('-inf'), float('+inf'))


def isValidBST_naive(root: Optional[TreeNode]) -> bool:
    """
    doesn't work with test 4
    """
    def dfs(root):
        if not root or (not root.left and not root.right):
            return True

        if not root.left and root.val >= root.right.val:
            return False
        if not root.left and root.val < root.right.val:
            return dfs(root.right)

        if not root.right and root.val <= root.left.val:
            return False
        if not root.right and root.val > root.left.val:
            return dfs(root.left)

        if mx and root.left <= mx:
            return False

        if root.val >= root.right.val or root.val <= root.left.val:
            return False
        else:
            return dfs(root.left) and dfs(root.right)

    return dfs(root)


if __name__ == '__main__':
    root = TreeNode(
        2,
        TreeNode(1),
        TreeNode(3)
    )
    assert True is isValidBST(root), 'test 1'

    root = TreeNode(
        2,
        TreeNode(2),
        TreeNode(2)
    )
    assert False is isValidBST(root), 'test 2'

    root = TreeNode(
        0,
        TreeNode(-1)
    )
    assert True is isValidBST(root), 'test 3'

    root = TreeNode(
        5,
        TreeNode(4),
        TreeNode(
            6,
            TreeNode(3),
            TreeNode(7)
        )
    )
    assert False is isValidBST(root), 'test 4'
