from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = [amount + 1 for _ in range(amount + 1)]
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != amount + 1 else -1


def coinChange_rec(coins: List[int], amount: int) -> int:
    def dfs(coins, amount, res):
        if amount < 0:
            return -1
        if amount == 0:
            return res
        tmp = [10000]
        for i in coins:
            tmp.append(dfs(coins, amount - i, res + 1))
        return min([i for i in tmp if i >= 0])
    return dfs(coins, amount, 0) if dfs(coins, amount, 0) != 10000 else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    assert 3 == coinChange(coins, amount), 'test 1'

    coins = [2]
    amount = 3
    assert -1 == coinChange(coins, amount), 'test 2'

    coins = [1]
    amount = 0
    assert 0 == coinChange(coins, amount), 'test 3'

    coins = [1, 2, 5]
    amount = 30
    assert 6 == coinChange(coins, amount), 'test 4'
