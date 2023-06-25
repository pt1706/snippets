def isSubsequence(s: str, t: str) -> bool:
    st = 0
    for digit in s:
        for i in range(st, len(t)):
            if t[i] == digit:
                st = i + 1
                break
        else:
            return False
    return True


if __name__ == '__main__':
    s = 'abc'
    t = 'ahbgdc'
    assert True is isSubsequence(s, t), 'test 1'
