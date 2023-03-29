from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def to_list(p):
        if not p:
            return [None]
        return [p.val] + to_list(p.left) + to_list(p.right)

    return to_list(p) == to_list(q)


if __name__ == '__main__':
    p = TreeNode(1, None, TreeNode(3, TreeNode(2, None, None), None))
    q = TreeNode(1, None, TreeNode(3, TreeNode(2, None, None), None))
    assert True is isSameTree(p, q)

    p = TreeNode(2, None, TreeNode(3, TreeNode(2, None, None), None))
    q = TreeNode(1, None, TreeNode(3, TreeNode(2, None, None), None))
    assert False is isSameTree(p, q)

    p = TreeNode(1, TreeNode(2, None, None), TreeNode(2, None, None))
    q = TreeNode(1, TreeNode(2, None, None), TreeNode(2, None, None))
    assert True is isSameTree(p, q)

    p = TreeNode(1, TreeNode(2, None, None), None)
    q = TreeNode(1, None, TreeNode(2, None, None))
    assert False is isSameTree(p, q)
