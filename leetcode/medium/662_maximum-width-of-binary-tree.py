from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
    """
    can't understand
    """
    res = 0
    q = deque([[root, 1, 0]])
    prevnum, prevlevel = 1, 0
    while q:
        node, num, level = q.popleft()

        if level > prevlevel:
            prevlevel = level
            prevnum = num

        res = max(res, num - prevnum + 1)
        if node.left:
            q.append([node.left, 2 * num, level + 1])
        if node.right:
            q.append([node.right, 2 * num + 1, level + 1])
    return res


def widthOfBinaryTree_my_v(root: Optional[TreeNode]) -> int:
    """
    can't pass time limit due to create all subnodes
    """
    q = []
    nq = [root]
    res = len(nq)
    while nq or q:
        tmp = []
        q = nq[:]
        nq = []
        while q:
            node = q.pop(0)
            if node.left:
                nq.extend(tmp)
                tmp = []
                nq.append(node.left)
            elif nq:
                tmp.append(TreeNode())

            if node.right:
                nq.extend(tmp)
                tmp = []
                nq.append(node.right)
            elif nq:
                tmp.append(TreeNode())
        res = max(res, len(nq))
    return res


if __name__ == '__main__':
    root = TreeNode(
        1,
        TreeNode(
            3,
            TreeNode(5, None, None),
            TreeNode(3, None, None)
        ),
        TreeNode(
            2,
            None,
            TreeNode(9, None, None)
        )
    )

    assert 4 == widthOfBinaryTree(root)