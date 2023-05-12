def numTrees(n: int) -> int:
    def dfs(nums, res):
        if len(nums) == 0:
            return res
        if len(nums) == 1:
            return res
        if len(nums) == 2:
            return res + 2
        for i in range(len(nums)):
            res += dfs(nums[:i], res) + dfs(nums[i + 1:], res)
        return res

    res = 0
    nums = [x for x in range(1, n + 1)]
    for i in range(len(nums)):
        res += 1 + dfs(nums[:i], res) + dfs(nums[i + 1:], res)
    return res


if __name__ == '__main__':
    n = 1
    assert 1 == numTrees(n), 'test 1'

    n = 3
    print(numTrees(n))
    assert 5 == numTrees(n), 'test 2'
