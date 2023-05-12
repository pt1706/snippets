from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMode(root: Optional[TreeNode]) -> List[int]:
    res = {}

    def dfs(node):
        nonlocal res
        if not node:
            return 0
        res[node.val] = res.get(node.val, 0) + 1
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    mx = max(res.values())
    d = [k for k, v in res.items() if v == mx]
    return d


if __name__ == '__main__':
    root = TreeNode(
        1,
        None,
        TreeNode(
            2,
            TreeNode(2),
            None
        ),
    )
    assert [2] == findMode(root), 'test 1'
