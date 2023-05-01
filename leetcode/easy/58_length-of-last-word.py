def lengthOfLastWord(s: str) -> int:
    lst = s.split()
    try:
        res = len(lst[-1])
    except Exception:
        return 0
    return res


if __name__ == '__main__':
    s = "Hello\nWor\nld"
    assert 2 == lengthOfLastWord(s)

    s = "Hello World"
    assert 5 == lengthOfLastWord(s)

    s = "   fly me   to   the moon  "
    assert 4 == lengthOfLastWord(s)

    s = "luffy is still joyboy"
    assert 6 == lengthOfLastWord(s)

    s = " "
    assert 0 == lengthOfLastWord(s)

    s = ""
    assert 0 == lengthOfLastWord(s)

    s = " t"
    assert 1 == lengthOfLastWord(s)