from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longestZigZag(root: Optional[TreeNode]) -> int:
    def dfs(root, res, d=None):
        if not root:
            return res

        if d == 'r':
            left = dfs(root.left, res + 1, 'l')
            right = dfs(root.right, 0, 'r')
        elif d == 'l':
            right = dfs(root.right, res + 1, 'r')
            left = dfs(root.left, 0, 'l')
        else:
            left = dfs(root.left, 0, 'l')
            right = dfs(root.right, 0, 'r')

        return max(left, right)
    return dfs(root, 0)


def longestZigZag_l(root: Optional[TreeNode]) -> int:
    def dfs(root, res, d=None):
        if not root:
            return res

        if d is None:
            if root.left is not None:
                left = dfs(root.left, 1, 'l')
            else:
                left = 0
            if root.right is not None:
                right = dfs(root.right, 1, 'r')
            else:
                right = 0
            return max(left, right)

        if d == 'r':
            if root.left is not None:
                left = dfs(root.left, res + 1, 'l')
            else:
                left = res
            if root.right is not None:
                right = dfs(root.right, 1, 'r')
            else:
                right = 0
            return max(left, right)

        if d == 'l':
            if root.left is not None:
                left = dfs(root.left, 1, 'l')
            else:
                left = 0
            if root.right is not None:
                right = dfs(root.right, res + 1, 'r')
            else:
                right = res
            return max(left, right)

    return dfs(root, 0)


def longestZigZag_two_rec(root: Optional[TreeNode]) -> int:
    def dfs_d(root, d):
        if not root:
            return 0
        if d == 'r':
            return 1 + dfs_d(root.left, 'l')
        if d == 'l':
            return 1 + dfs_d(root.right, 'r')

    def dfs(root, res):
        if not root:
            return res
        new_res = max(dfs_d(root.left, 'l'), dfs_d(root.right, 'r'))
        if new_res > res:
            return max(dfs(root.left, new_res), dfs(root.right, new_res))
        return max(dfs(root.left, res), dfs(root.right, res))

    return dfs(root, 0)

if __name__ == '__main__':
    root = TreeNode(
        1,
        TreeNode(
            1,
            None,
            TreeNode(
                1,
                TreeNode(
                    1,
                    None,
                    TreeNode(1, None, None)
                ),
                TreeNode(1, None, None)
            ),
        ),
        TreeNode(1, None, None)
    )
    assert 4 == longestZigZag(root)