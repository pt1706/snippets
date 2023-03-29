from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []

    def inner(root):
        if not root:
            return None
        inner(root.left)
        res.append(root.val)
        inner(root.right)

    inner(root)
    return res


if __name__ == '__main__':
    root = TreeNode(1)
    assert [1] == inorderTraversal(root)

    root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
    assert [1, 3, 2] == inorderTraversal(root)
