def longestPalindrome(s: str) -> str:
    res = ''
    for i in range(len(s)):
        r, l = i, i
        while r >= 0 and l < len(s) and s[r] == s[l]:
            if l - r + 1 > len(res):
                res = s[r: l + 1]
            r -= 1
            l += 1

        r, l = i, i + 1
        while r >= 0 and l < len(s) and s[r] == s[l]:
            if l - r + 1 > len(res):
                res = s[r: l + 1]
            r -= 1
            l += 1

    return res


def longestPalindrome_dp(s: str) -> str:
    """
    doesn't work with s = "aacabdkacaa"
    """
    t = s[::-1]
    res = ''
    m = [['' for i in range(len(s) + 1)] for j in range(len(s) + 1)]
    for i in range(len(s) - 1, -1, -1):
        for j in range(len(s) - 1, -1, -1):
            i_1 = s[i]
            i_2 = t[j]
            if i_1 == i_2:
                m[i][j] = m[i + 1][j + 1] + s[i]
                if len(m[i][j]) > len(res):
                    res = m[i][j]
    return res


def longestPalindrome_iter(s: str) -> str:
    res = ''
    while s and len(s) > len(res):
        t = s
        while t and len(t) > len(res):
            if t == t[::-1]:
                res = t
            t = t[:-1]
        s = s[1:]
    return res


if __name__ == '__main__':
    s = 'babad'
    assert longestPalindrome(s) in ['bab', 'aba'], 'test 1'

    s = 'cbbd'
    assert longestPalindrome(s) in ['bb'], 'test 2'
