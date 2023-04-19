def isIsomorphic(s: str, t: str) -> bool:
    d = {}
    for i in range(len(s)):
        if d.get(t[i]):
            if d[t[i]] != s[i]:
                return False
        else:
            d[t[i]] = s[i]

    d = {v: k for k, v in d.items()}
    for i in range(len(t)):
        if d.get(s[i]):
            if d[s[i]] != t[i]:
                return False
    return True


if __name__ == '__main__':
    s = 'badc'
    t = 'baba'
    assert False is isIsomorphic(s, t), 'test 1'

    s = 'paper'
    t = 'title'
    assert True is isIsomorphic(s, t), 'test 2'

    s = 'foo'
    t = 'bar'
    assert False is isIsomorphic(s, t), 'test 3'