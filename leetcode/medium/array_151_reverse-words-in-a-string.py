from collections import deque


def reverseWords(s: str) -> str:
    res = deque()
    l, r = 0, 1
    for r in range(len(s)):
        if not s[l].isalnum() and not s[r].isalnum():
            l = r
        if not s[l].isalnum() and s[r].isalnum():
            l = r
        if s[l].isalnum() and not s[r].isalnum():
            word = s[l:r]
            res.appendleft(word)
            l = r
        if s[l].isalnum() and r == len(s) - 1:
            word = s[l:r + 1]
            res.appendleft(word)
            l = r
    return ' '.join(res)


if __name__ == '__main__':
    s = 'the sky is blue'
    res = 'blue is sky the'
    assert res == reverseWords(s), 'test 1'

    s = '  hello world  '
    res = 'world hello'
    assert res == reverseWords(s), 'test 2'

    s = 'a good   example'
    res = 'example good a'
    assert res == reverseWords(s), 'test 3'