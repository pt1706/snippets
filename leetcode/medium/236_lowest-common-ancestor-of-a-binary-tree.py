class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        res = f'val={self.val};'
        if self.left:
            res += f' left={self.left.val};'
        if self.right:
            res += f' right={self.right.val};'
        return res


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def is_same(f, s):
        if f is None and s is None:
            return True
        if f is None or s is None or f.val != s.val:
            return False
        return is_same(f.left, s.left) and is_same(f.right, s.right)

    def in_tree(f, s):
        if f is None and s is None:
            return True
        if f is None or s is None:
            return False
        if is_same(f, s):
            return True
        return in_tree(f.left, s) or in_tree(f.right, s)

    def dfs(root, p, q):
        if root is None:
            return
        if (in_tree(root.left, p) and in_tree(root.right, q)) or (in_tree(root.right, p) and in_tree(root.left, q)):
            return root
        if in_tree(root.left, p) and in_tree(root.left, q):
            return dfs(root.left, p, q)
        return dfs(root.right, p, q)

    if in_tree(p, q):
        return p
    if in_tree(q, p):
        return q

    return dfs(root, p, q)


if __name__ == '__main__':
    root = TreeNode(
        3,
        TreeNode(
            5,
            TreeNode(6),
            TreeNode(
                2,
                TreeNode(7),
                TreeNode(4)
            )
        ),
        TreeNode(
            1,
            TreeNode(0),
            TreeNode(8)
        )
    )
    p = root.left

    q = root.right
    assert root == lowestCommonAncestor(root, p, q), 'test 1'

    p = root.left
    q = root.left.right.right
    assert p == lowestCommonAncestor(root, p, q), 'test 2'

    root = TreeNode(
        1,
        TreeNode(2),
        None
    )

    p = root
    q = root.left
    assert root == lowestCommonAncestor(root, p, q), 'test 3'

