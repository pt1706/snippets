from typing import List


def stoneGame(piles: List[int]) -> bool:
    def dfs(l, r):
        if r - l < 1:
            return 0

        if (l, r) in dp:
            return dp[(l, r)]
        else:
            if (r - l + 1) % 2 == 0:
                first = piles[l] + dfs(l + 1, r)
                tail = piles[r] + dfs(l, r - 1)
                dp[(l, r)] = max(first, tail)
            else:
                first = dfs(l + 1, r)
                tail = dfs(l, r - 1)
                dp[(l, r)] = max(first, tail)
            return dp[(l, r)]
    dp = {}
    piles = tuple(piles)
    return dfs(0, len(piles) - 1) > sum(piles) // 2


def stoneGame_simpliest(piles: List[int]) -> bool:
    return True


def stoneGame_simple(piles: List[int]) -> bool:
    """timelimit"""
    def dfs(piles, dif, k):
        if not len(piles):
            return True if dif > 0else False
        if (piles, dif, k) in dp:
            return dp[(piles, dif, k)]
        f = dfs(piles[1:], dif - k * piles[0], k * -1)
        l = dfs(piles[:-1], dif - k * piles[-1], k * -1)
        dp[(piles, dif, k)] = f or l
        return dp[(piles, dif, k)]
    dp = {}
    piles = tuple(piles)
    return dfs(piles, 0, -1)


if __name__ == '__main__':
    piles = [5, 3, 4, 5]
    assert True is stoneGame(piles), 'test 1'

    piles = [3, 7, 2, 3]
    assert True is stoneGame(piles), 'test 2'

    piles = [7, 7, 12, 16, 41, 48, 41, 48, 11, 9, 34, 2, 44, 30,
             27, 12, 11, 39, 31, 8, 23, 11, 47, 25, 15, 23, 4,
             17, 11, 50, 16, 50, 38, 34, 48, 27, 16, 24, 22, 48,
             50, 10, 26, 27, 9, 43, 13, 42, 46, 24]
    assert True is stoneGame(piles), 'test 3'

    piles = [8, 9, 7, 6, 7, 6]
    assert True is stoneGame(piles), 'test 4'
