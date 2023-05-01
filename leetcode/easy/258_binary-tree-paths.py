from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    res = []
    path = f'{root.val}'

    def dfs(root, path):
        if not root.left and not root.right:
            res.append(path)
            return None
        if root.left:
            path_l = path + f'->{root.left.val}'
            dfs(root.left, path_l)
        if root.right:
            path_r = path + f'->{root.right.val}'
            dfs(root.right, path_r)
        return None

    dfs(root, path)
    return res


if __name__ == '__main__':
    res = ['1->2->5', '1->3']
    root = TreeNode(
        1,
        TreeNode(
            2,
            None,
            TreeNode(
                5,
                None,
                None
            )
        ),
        TreeNode(
            3,
            None,
            None
        ),
    )
    assert res == binaryTreePaths(root), '1 test'