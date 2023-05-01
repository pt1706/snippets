def countSubstrings(s: str) -> int:
    res = 0
    for i in range(len(s)):
        r, l = i, i
        while r >= 0 and l < len(s) and s[r] == s[l]:
            res += 1
            r -= 1
            l += 1

        r, l = i, i + 1
        while r >= 0 and l < len(s) and s[r] == s[l]:
            res += 1
            r -= 1
            l += 1
    return res


if __name__ == '__main__':
    s = 'abc'
    assert 3 == countSubstrings(s), 'test 1'

    s = 'aaa'
    assert 6 == countSubstrings(s), 'test 2'