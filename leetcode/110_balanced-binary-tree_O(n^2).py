from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: Optional[TreeNode]):
    def dfs(root):
        if not root:
            return 0
        return 1 + max(dfs(root.left), dfs(root.right))
    if not root:
        return True
    res = dfs(root.left) - dfs(root.right)
    if abs(res) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)


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
    print(isBalanced(root))

