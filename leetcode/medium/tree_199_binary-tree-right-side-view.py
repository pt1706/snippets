from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res = []
    q = deque()
    q.append(root)
    n_q = []
    while q:
        res.append(q[-1].val)
        while q:
            node = q.popleft()
            if node.left:
                n_q.append(node.left)
            if node.right:
                n_q.append(node.right)
        q.extend(n_q)
        n_q = []
    return res


if __name__ == '__main__':
    root = TreeNode(
        1,
        TreeNode(
            2,
            None,
            TreeNode(5)
        ),
        TreeNode(
            3,
            None,
            TreeNode(4)
        )
    )
    assert [1, 3, 4] == rightSideView(root), 'test 1'

    root = TreeNode(
        1,
        None,
        TreeNode(3)
    )
    assert [1, 3] == rightSideView(root), 'test 2'

    root = None
    assert [] == rightSideView(root), 'test 3'

    root = TreeNode(
        1,
        TreeNode(
            2,
            None,
            TreeNode(
                5,
                TreeNode(7),
                None
            )
        ),
        TreeNode(
            3,
            None,
            TreeNode(4)
        )
    )
    assert [1, 3, 4, 7] == rightSideView(root), 'test 4'