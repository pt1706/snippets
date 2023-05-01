def numDecodings(s: str) -> int:
    """
    rec_cash
    """
    dp = {}

    def dfs(s):
        if not s:
            return 1
        if s[0] == '0':
            return 0
        if len(s[:2]) == 2 and s[:2] < '27':
            if not dp.get(s[1:]):
                dp[s[1:]] = dfs(s[1:])
            f = dp.get(s[1:])

            if not dp.get(s[2:]):
                dp[s[2:]] = dfs(s[2:])
            s = dp.get(s[2:])
            return f + s
        else:
            if not dp.get(s[1:]):
                dp[s[1:]] = dfs(s[1:])
            f = dp.get(s[1:])
            return f
    return dfs(s)


if __name__ == '__main__':
    s = '12'
    assert 2 == numDecodings(s), 'test 1'

    s = '226'
    assert 3 == numDecodings(s), 'test 2'

    s = '10'
    assert 1 == numDecodings(s), 'test 3'

    s = '111111111111111111111111111111111111111111111'
    assert 1836311903 == numDecodings(s), 'test 4'
