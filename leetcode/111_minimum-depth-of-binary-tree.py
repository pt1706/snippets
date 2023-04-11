from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: Optional[TreeNode]) -> int:
    def dfs(root):
        if not root.left and not root.right:
            return 1
        if root.left and root.right:
            return 1 + min(dfs(root.left), dfs(root.right))
        if root.left:
            return 1 + dfs(root.left)
        if root.right:
            return 1 + dfs(root.right)

    if not root:
        return 0
    return dfs(root)


if __name__ == '__main__':
    root = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(3, TreeNode(3, None, None), None),
            None
        ),
        TreeNode(2, None, None)
    )
    assert 2 == minDepth(root)

    root = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(
                3,
                TreeNode(
                    4,
                    TreeNode(
                        5,
                        None,
                        None
                    ),
                    None
                ),
                None
            ),
            None
        ),
        None
    )
    assert 5 == minDepth(root)


