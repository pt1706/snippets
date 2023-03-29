from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:
    def do_check(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (
                left.val == right.val and
                do_check(left.left, right.right) and
                do_check(left.right, right.left)
        )

    return do_check(root.left, root.right)


if __name__ == '__main__':
    root = TreeNode(1, None, TreeNode(3, TreeNode(2, None, None), None))
    assert False is isSymmetric(root)

    root = TreeNode(1, TreeNode(2, None, None), TreeNode(2, None, None))
    assert True is isSymmetric(root)

    root = TreeNode(1, TreeNode(2, TreeNode(3, None, None), None), TreeNode(2, None, None))
    assert False is isSymmetric(root)

    root = TreeNode(
        1,
        TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)),
        TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None))
    )
    assert True is isSymmetric(root)

    root = TreeNode(
        1,
        TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)),
        TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None))
    )
    assert False is isSymmetric(root)