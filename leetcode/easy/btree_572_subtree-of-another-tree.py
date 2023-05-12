from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isSame(r, s):
        if not r and not s:
            return True
        if (not r and s) or (r and not s):
            return False
        if r.val != s.val:
            return False
        return isSame(r.left, s.left) and isSame(r.right, s.right)

    if not root and not subRoot:
        return True
    if not root:
        return False
    if isSame(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


if __name__ == '__main__':
    root = TreeNode(
        3,
        TreeNode(
            4,
            TreeNode(1, None, None),
            TreeNode(2, None, None)
        ),
        TreeNode(5, None, None)
    )
    subRoot = TreeNode(
            4,
            TreeNode(1, None, None),
            TreeNode(2, None, None)
        )
    assert True is isSubtree(root, subRoot), '1 test'