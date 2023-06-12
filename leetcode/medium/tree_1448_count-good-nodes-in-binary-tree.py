class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root: TreeNode) -> int:
    if not root:
        return 0

    def dfs(node, mx):
        if not node:
            return 0
        if node.val < mx:
            return dfs(node.left, mx) + dfs(node.right, mx)
        mx = max(mx, node.val)
        return 1 + dfs(node.left, mx) + dfs(node.right, mx)

    return dfs(root, root.val)


if __name__ == '__main__':
    root = TreeNode(
        3,
        TreeNode(
            1, TreeNode(3)
        ),
        TreeNode(
            4,
            TreeNode(1),
            TreeNode(5)
        )
    )
    assert 4 == goodNodes(root), 'test 1'