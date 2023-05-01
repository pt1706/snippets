from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


if __name__ == '__main__':
    root = TreeNode(1, None, TreeNode(3, TreeNode(2, None, None), None))
    assert 3 == maxDepth(root)

    root = TreeNode(1, TreeNode(2, None, None), TreeNode(2, None, None))
    assert 2 == maxDepth(root)

    root = TreeNode(1, TreeNode(2, TreeNode(3, None, None), None), TreeNode(2, None, None))
    assert 3 == maxDepth(root)

    root = TreeNode()
    assert 1 == maxDepth(root)
