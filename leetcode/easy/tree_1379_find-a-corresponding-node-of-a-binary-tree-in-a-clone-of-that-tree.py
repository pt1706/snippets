class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    def is_same(n_1, n_2):
        if not n_1 and not n_2:
            return True
        if not n_1 or not n_2:
            return False
        if n_1.val != n_2.val:
            return False
        return is_same(n_1.left, n_2.left) and is_same(n_1.right, n_2.right)

    def dfs(node):
        if is_same(node, target):
            return node
        if not node:
            return False
        return dfs(node.right) or dfs(node.left)

    return dfs(cloned)

if __name__ == '__main__':
    pass