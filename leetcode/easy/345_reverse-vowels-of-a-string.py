def reverseVowels(s: str) -> str:
    d = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    l = 0
    r = len(s) - 1
    s = list(s)
    while l <= r:
        while l <= r and s[l] not in d:
            l += 1
        while l <= r and s[r] not in d:
            r -= 1
        if l >= r:
            break
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    return ''.join(s)


if __name__ == '__main__':
    s = "hello"
    res = "holle"
    assert res == reverseVowels(s), 'test 1'

    s = "leetcode"
    res = "leotcede"
    assert res == reverseVowels(s), 'test 1'