def removeStars(s: str) -> str:
    while s:
        i = s.find('*')
        if i == -1:
            break
        s = s[:i - 1] + s[i + 1:]
    return s


if __name__ == '__main__':
    s = 'leet**cod*e'
    assert 'lecoe' == removeStars(s), 'test 1'

    s = 'erase*****'
    assert '' == removeStars(s), 'test 2'