from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'val: {self.val}'


def maxDepth(root: Optional[TreeNode]) -> int:
    depth = 0
    queue = [root]
    next_q = []
    while next_q or queue:
        depth += 1
        while queue:
            print(f'depth {depth}, next_q: {next_q}, queue: {queue}')
            item = queue.pop()
            if item.left:
                next_q.append(item.left)
            if item.right:
                next_q.append(item.right)
        queue = next_q
        next_q = []
    return depth


if __name__ == '__main__':
    root = TreeNode(
        3,
        TreeNode(9, None, None),
        TreeNode(
            20,
            TreeNode(15, None, None),
            TreeNode(7, None, None)
        )
    )
    assert 3 == maxDepth(root)

    root = TreeNode(1, None, TreeNode(3, TreeNode(2, None, None), None))
    assert 3 == maxDepth(root)

    root = TreeNode(1, TreeNode(2, None, None), TreeNode(2, None, None))
    assert 2 == maxDepth(root)

    root = TreeNode(1, TreeNode(2, TreeNode(3, None, None), None), TreeNode(2, None, None))
    assert 3 == maxDepth(root)

    root = TreeNode()
    assert 1 == maxDepth(root)
