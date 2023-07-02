from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        res = f'val = {self.val}'
        if self.left:
            res += f', left = {self.left.val}'
        if self.right:
            res += f', right = {self.right.val}'
        return res


def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    res = 0

    def dfs(node, t):
        nonlocal res
        if not node:
            return
        t -= node.val
        if t == 0:
            res += 1
        dfs(node.left, t)
        dfs(node.right, t)

    def helper(node):
        if not node:
            return
        dfs(node, targetSum)
        helper(node.left)
        helper(node.right)

    helper(root)
    return res


if __name__ == '__main__':
    root = TreeNode(
        10,
        TreeNode(
            5,
            TreeNode(
                3,
                TreeNode(3),
                TreeNode(-2)
            ),
            TreeNode(
                2,
                None,
                TreeNode(1)
            )
        ),
        TreeNode(
            -3,
            None,
            TreeNode(11),
        )
    )
    assert 3 == pathSum(root, 8), 'test 1'

    root = TreeNode(
        1,
        None,
        TreeNode(
            2,
            None,
            TreeNode(
                3,
                None,
                TreeNode(
                    4,
                    None,
                    TreeNode(5)
                )
            ),
        )
    )
    assert 2 == pathSum(root, 3), 'test 2'

    root = TreeNode(
        0,
        TreeNode(1),
        TreeNode(1)
    )
    assert 4 == pathSum(root, 1), 'test 3'
