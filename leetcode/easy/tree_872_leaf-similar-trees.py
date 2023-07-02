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


def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    leaf_1 = []
    leaf_2 = []

    def dfs(node, leaf):
        if not node.left and not node.right:
            leaf.append(node.val)
            return leaf
        if node.left:
            leaf = dfs(node.left, leaf)
        if node.right:
            leaf = dfs(node.right, leaf)
        return leaf

    return dfs(root1, leaf_1) == dfs(root2, leaf_2)


if __name__ == '__main__':
    root_1 = TreeNode(
        3,
        TreeNode(
            5,
            TreeNode(6),
            TreeNode(
                2,
                TreeNode(7),
                TreeNode(4)
            )
        ),
        TreeNode(
            1,
            TreeNode(9),
            TreeNode(8),
        )
    )
    root_2 = TreeNode(
        3,
        TreeNode(
            5,
            TreeNode(6),
            TreeNode(7)
        ),
        TreeNode(
            1,
            TreeNode(4),
            TreeNode(
                2,
                TreeNode(9),
                TreeNode(8)
            ),
        )
    )
    assert True is leafSimilar(root_1, root_2), 'test 1'