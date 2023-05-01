def lengthOfLongestSubstring(s: str) -> int:
    res = 0
    st = ''
    for i in s:
        while i in st:
            st = st[1:]
        st += i
        res = max(res, len(st))
    return res


def lengthOfLongestSubstring_1(s: str) -> int:
    res = 0
    while s:
        st = ''
        for i in s:
            if i in st:
                break
            st += i
            res = max(res, len(st))
        s = s[1:]
    return res


if __name__ == '__main__':
    s = 'abcabcbb'
    assert 3 == lengthOfLongestSubstring(s), '1 test'

    s = 'bbbbb'
    assert 1 == lengthOfLongestSubstring(s), '2 test'

    s = 'pwwkew'
    assert 3 == lengthOfLongestSubstring(s), '3 test'

