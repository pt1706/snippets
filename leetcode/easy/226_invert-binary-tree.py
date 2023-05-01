from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(node):
        if not node:
            return None
        save = node.left
        node.left = dfs(node.right)
        node.right = dfs(save)
        return node
    return dfs(root)


if __name__ == '__main__':
    root = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1, None, None),
            TreeNode(3, None, None),
        ),
        TreeNode(
            7,
            TreeNode(6, None, None),
            TreeNode(9, None, None),
        ),
    )

    res = TreeNode(
        4,
        TreeNode(
            7,
            TreeNode(9, None, None),
            TreeNode(6, None, None),
        ),
        TreeNode(
            2,
            TreeNode(3, None, None),
            TreeNode(1, None, None),
        ),
    )
    assert res == invertTree(root), '1 test'