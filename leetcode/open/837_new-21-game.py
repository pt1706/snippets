def new21Game(n: int, k: int, maxPts: int) -> float:
    dp = {}

    def dfs(score):
        if score >= k:
            return 1 if score <= n else 0
        if score in dp:
            return dp[score]
        prob = 0
        for i in range(1, maxPts + 1):
            prob += dfs(score + i)
        dp[score] = round(prob / maxPts, 5)
        return dp[score]

    return dfs(0)


if __name__ == '__main__':
    n = 10
    k = 1
    maxPts = 10
    assert 1.0 == new21Game(n, k, maxPts), 'test 1'

    n = 6
    k = 1
    maxPts = 10
    assert 0.6 == new21Game(n, k, maxPts), 'test 2'

    n = 21
    k = 17
    maxPts = 10
    assert 0.73278 == new21Game(n, k, maxPts), 'test 3'
