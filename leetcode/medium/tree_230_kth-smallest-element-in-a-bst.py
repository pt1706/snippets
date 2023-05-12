from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        curr = curr.right

def kthSmallest_rec(root: Optional[TreeNode], k: int) -> int:
    res = []

    def dfs(node):
        nonlocal res
        if not node:
            return 0
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res[k - 1]


if __name__ == '__main__':
    root = TreeNode(
        3,
        TreeNode(
            1,
            None,
            TreeNode(2)
        ),
        TreeNode(4)
    )
    k = 1
    assert 1 == kthSmallest(root, k), 'test 1'

    root = TreeNode(
        5,
        TreeNode(
            3,
            TreeNode(
                2,
                TreeNode(1),
                None
            ),
            TreeNode(4)
        ),
        TreeNode(6)
    )
    k = 3
    assert 3 == kthSmallest(root, k), 'test 2'