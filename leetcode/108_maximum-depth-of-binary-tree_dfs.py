from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'val: {self.val}'


def maxDepth(root: Optional[TreeNode]) -> int:
    stack = [[root, 1]]
    res = 0
    while stack:
        node, depth = stack.pop()
        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return res


if __name__ == '__main__':
    root = TreeNode(
        3,
        TreeNode(9, None, None),
        TreeNode(
            20,
            TreeNode(15, None, None),
            TreeNode(7, None, None)
        )
    )
    assert 3 == maxDepth(root)

    root = TreeNode(1, None, TreeNode(3, TreeNode(2, None, None), None))
    assert 3 == maxDepth(root)

    root = TreeNode(1, TreeNode(2, None, None), TreeNode(2, None, None))
    assert 2 == maxDepth(root)

    root = TreeNode(1, TreeNode(2, TreeNode(3, None, None), None), TreeNode(2, None, None))
    assert 3 == maxDepth(root)

    root = TreeNode()
    assert 1 == maxDepth(root)
