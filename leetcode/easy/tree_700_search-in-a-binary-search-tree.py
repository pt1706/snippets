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


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    def dfs(node, val):
        if not node:
            return None
        if node.val == val:
            return node
        return dfs(node.left, val) or dfs(node.right, val)

    return dfs(root, val)


if __name__ == '__main__':
    root = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(
            7,
            None,
            None,
        )
    )
    res = root.left
    assert res == searchBST(root, 2), 'test 1'