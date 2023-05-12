from typing import List


def maxUncrossedLines(nums1: List[int], nums2: List[int]) -> int:
    dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                dp[i + 1][j + 1] = 1 + dp[i][j]
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[len(nums1)][len(nums2)]


def maxUncrossedLines_rec(nums1: List[int], nums2: List[int]) -> int:
    dp = {}

    def dfs(i, j):
        if i == len(nums1) or j == len(nums2):
            return 0
        if (i, j) in dp:
            return dp[(i, j)]
        if nums1[i] == nums2[j]:
            dp[(i, j)] = 1 + dfs(i + 1, j + 1)
            return dp[(i, j)]
        else:
            dp[(i, j)] = max(dfs(i, j + 1), dfs(i + 1, j))
            return dp[(i, j)]

    return dfs(0, 0)


if __name__ == '__main__':
    nums1 = [2, 5, 1, 2, 5]
    nums2 = [10, 5, 2, 1, 5, 2]
    assert 3 == maxUncrossedLines(nums1, nums2), 'test 1'

    nums1 = [1, 3, 7, 1, 7, 5]
    nums2 = [1, 9, 2, 5, 1]
    assert 2 == maxUncrossedLines(nums1, nums2), 'test 2'
