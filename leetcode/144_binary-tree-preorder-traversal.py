from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    queue = [root]
    while queue:
        item = queue.pop()
        if not item:
            continue
        res.append(item.val)
        if item.right:
            queue.append(item.right)
        if item.left:
            queue.append(item.left)
    return res


def preorderTraversal_rec(root: Optional[TreeNode]) -> List[int]:
    def dfs(root):
        if not root:
            return []
        return [root.val] + dfs(root.left) + dfs(root.right)

    return dfs(root)


if __name__ == '__main__':
    res = [1, 2, 3]
    root = TreeNode(
        1,
        None,
        TreeNode(
            2,
            TreeNode(3, None, None),
            None
        ),
    )
    assert res == preorderTraversal(root), '1 test'

    res = [1]
    root = TreeNode(
        1,
        None,
        None
    )
    assert res == preorderTraversal(root), '2 test'

    res = []
    root = None
    assert res == preorderTraversal(root), '3 test'

    res = [3, 1, 2]
    root = TreeNode(
        3,
        TreeNode(1, None, None),
        TreeNode(2, None, None),
    )
    assert res == preorderTraversal(root), '4 test'

    res = [1, 4, 2, 3]
    root = TreeNode(
        1,
        TreeNode(4, TreeNode(2, None, None), None),
        TreeNode(3, None, None),
    )
    assert res == preorderTraversal(root), '5 test'

