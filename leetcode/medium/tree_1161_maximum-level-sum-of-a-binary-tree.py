from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxLevelSum(root: Optional[TreeNode]) -> int:
    res = (float('-inf'), 0)
    lev = 0
    q = [root]
    n_q = []
    while q or n_q:
        lev += 1
        s_lev = 0
        while q:
            item = q.pop()
            s_lev += item.val
            if item.left:
                n_q.append(item.left)
            if item.right:
                n_q.append(item.right)
        if s_lev > res[0]:
            res = (s_lev, lev)
        q = n_q
        n_q = []

    return res[1]


if __name__ == '__main__':
    root = TreeNode(
        1,
        TreeNode(
            7,
            TreeNode(7),
            TreeNode(-8)
        ),
        TreeNode(0)
    )
    assert 2 == maxLevelSum(root), 'test 1'