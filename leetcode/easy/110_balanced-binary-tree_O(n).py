from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: Optional[TreeNode]):
    def dfs(root):
        if not root:
            return [True, 0]
        left = dfs(root.left)
        right = dfs(root.right)
        balanced = all([left[0], right[0], abs(left[1] - right[1]) <= 1])
        return [balanced, 1 + max(left[1], right[1])]
    return dfs(root)[0]


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

