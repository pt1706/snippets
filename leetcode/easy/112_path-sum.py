from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(cur_sum, root):
        if not root:
            return False
        cur_sum += root.val
        if not root.left and not root.right:
            return cur_sum == targetSum
        if root.left or root.right:
            return dfs(cur_sum, root.left) or dfs(cur_sum, root.right)

    cur_sum = 0
    return dfs(cur_sum, root)


if __name__ == '__main__':
    root = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(
                3,
                TreeNode(
                    3,
                    None,
                    None
                ),
                None
            ),
            None
        ),
        TreeNode(2, None, None)
    )
    assert True is hasPathSum(root, 9)
    assert True is hasPathSum(root, 3)
    assert False is hasPathSum(root, 5)

    root = TreeNode()
    assert True is hasPathSum(root, 0)

    root = TreeNode(
        1,
        TreeNode(
            2,
            None,
            None
        ),
        None
    )
    assert False is hasPathSum(root, 1)