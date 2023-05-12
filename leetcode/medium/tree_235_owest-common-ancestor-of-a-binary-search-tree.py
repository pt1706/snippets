class TreeNode:
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


def lowestCommonAncestor(root, p, q):
    """
    iter
    """
    cur = root
    while cur:
        if p.val < cur.val and q.val < cur.val:
            cur = cur.left
        elif p.val > cur.val and q.val > cur.val:
            cur = cur.right
        else:
            return cur


def lowestCommonAncestor_rec(root, p, q):
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor_rec(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lowestCommonAncestor_rec(root.right, p, q)
    else:
        return root


def lowestCommonAncestor_simple(root, p, q):
    if p.val == root.val or \
            q.val == root.val or \
            (p.val < root.val and q.val > root.val) or \
            (p.val > root.val and q.val < root.val):
        return root
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor_simple(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor_simple(root.right, p, q)


if __name__ == '__main__':
    root = TreeNode(
        6,
        TreeNode(
            2,
            TreeNode(0),
            TreeNode(
                4,
                TreeNode(3),
                TreeNode(5)
            )
        ),
        TreeNode(
            8,
            TreeNode(7),
            TreeNode(9)
        )
    )
    p = TreeNode(
            2,
            TreeNode(0),
            TreeNode(
                4,
                TreeNode(3),
                TreeNode(5)
            )
        )
    q = TreeNode(
            8,
            TreeNode(7),
            TreeNode(9)
        )
    res = TreeNode(
        6,
        TreeNode(
            2,
            TreeNode(0),
            TreeNode(
                4,
                TreeNode(3),
                TreeNode(5)
            )
        ),
        TreeNode(
            8,
            TreeNode(7),
            TreeNode(9)
        )
    )
    assert res == lowestCommonAncestor(root, p, q)