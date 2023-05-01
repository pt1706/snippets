from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    queue = [root]
    while queue:
        item = queue.pop()
        if not item:
            continue
        res.append(item)
        if item.left:
            queue.append(item.left)
        if item.right:
            queue.append(item.right)
    return [item.val for item in res[::-1]]


def postorderTraversal_rec(root: Optional[TreeNode]) -> List[int]:
    def dfs(root):
        if not root:
            return []
        return dfs(root.left) + dfs(root.right) + [root.val]

    return dfs(root)


if __name__ == '__main__':
    res = [3, 2, 1]
    root = TreeNode(
        1,
        None,
        TreeNode(
            2,
            TreeNode(3, None, None),
            None
        ),
    )
    assert res == postorderTraversal(root), '1 test'

    res = [1]
    root = TreeNode(
        1,
        None,
        None
    )
    assert res == postorderTraversal(root), '2 test'

    res = []
    root = None
    assert res == postorderTraversal(root), '3 test'

    res = [1, 2, 3]
    root = TreeNode(
        3,
        TreeNode(1, None, None),
        TreeNode(2, None, None),
    )
    assert res == postorderTraversal(root), '4 test'
