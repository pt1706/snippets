from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        res = 'Instance: '

        def helper(root):
            nonlocal res
            if not root:
                return 'None'
            else:
                res += f'{root.val}'
            if root.left:
                res += ', left: '
                helper(root.left)
            if root.right:
                res += ', right: '
                helper(root.right)
        helper(self)
        return str(res)


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def create_node(nums):
        if not nums:
            return None
        midle = (len(nums) - 1) // 2
        root = TreeNode(nums[midle])
        root.left = create_node(nums[:midle])
        root.right = create_node(nums[midle + 1:])
        return root

    return create_node(nums)


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    res = TreeNode(
        0,
        TreeNode(
            -10,
            None,
            TreeNode(-3, None, None)
        ),
        TreeNode(
            5,
            None,
            TreeNode(9, None, None)
        )
    )
    assert res.__repr__() == sortedArrayToBST(nums).__repr__()