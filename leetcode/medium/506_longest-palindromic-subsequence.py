def longestPalindromeSubseq(s: str) -> int:
    def lcs(s, t):
        res = [[0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    res[i][j] = 1 + res[i + 1][j + 1]
                else:
                    res[i][j] = max(res[i][j + 1], res[i + 1][j])
        return res[0][0]

    return lcs(s, s[::-1])


if __name__ == '__main__':
    s = 'bbbab'
    assert 4 == longestPalindromeSubseq(s), 'test 1'

    s = 'cbbd'
    assert 2 == longestPalindromeSubseq(s), 'test 2'