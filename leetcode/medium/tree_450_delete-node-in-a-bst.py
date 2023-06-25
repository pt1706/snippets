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


def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return root

    if root.val == key:
        if not root.right:
            return root.left
        cur = root.right
        while cur.left:
            cur = cur.left
        cur.left = root.left
        return root.right

    def dfs(node, k):
        if not node:
            return None
        if node.left and node.left.val == k:
            return (node, 'l')
        if node.right and node.right.val == k:
            return (node, 'r')
        if k > node.val:
            return dfs(node.right, k)
        return dfs(node.left, k)

    node, d = dfs(root, key)
    if not node:
        return root

    if d == 'l':
        deleted = node.left
        if not deleted.right:
            node.left = deleted.left
            return root
        cur = deleted.right
        while cur.left:
            cur = cur.left
        cur.left = deleted.left
        node.left = deleted.right
        return root

    deleted = node.right
    if not deleted.left:
        node.right = deleted.right
        return root
    cur = deleted.left
    while cur.right:
        cur = cur.right
    cur.right = deleted.right
    node.right = deleted.left
    return root


if __name__ == '__main__':
    root = TreeNode(
        5,
        TreeNode(
            3,
            TreeNode(2),
            TreeNode(4)
        ),
        TreeNode(
            6,
            None,
            TreeNode(7)
        )
    )
    res = TreeNode(
        5,
        TreeNode(
            4,
            TreeNode(2),
            None
        ),
        TreeNode(
            6,
            None,
            TreeNode(7)
        )
    )
    assert res == deleteNode(root, 3), 'test 1'

    root = TreeNode(
        5,
        TreeNode(
            2,
            None,
            TreeNode(4)
        ),
        TreeNode(
            6,
            None,
            TreeNode(7)
        )
    )
    assert root == deleteNode(root, 0), 'test 2'

    assert None is deleteNode(None, 0), 'test 3'

    root = TreeNode(
        5,
        TreeNode(
            3,
            TreeNode(2),
            TreeNode(4)
        ),
        TreeNode(
            6,
            None,
            TreeNode(7)
        )
    )
    res = TreeNode(
        5,
        TreeNode(
            3,
            TreeNode(2),
            TreeNode(4)
        ),
        TreeNode(
            6,
            None,
            None
        )
    )
    assert res == deleteNode(root, 7), 'test 4'
