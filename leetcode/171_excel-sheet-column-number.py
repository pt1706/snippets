def titleToNumber(columnTitle: str) -> int:
    res = 0
    mult = 0
    while columnTitle:
        res += (ord(columnTitle[-1]) - 64) * 26 ** mult
        mult += 1
        columnTitle = columnTitle[:-1]
    return res


if __name__ == '__main__':
    columnTitle = 'A'
    assert 1 == titleToNumber(columnTitle), 'test 1'

    columnTitle = 'AB'
    assert 28 == titleToNumber(columnTitle), 'test 2'

    columnTitle = 'ZY'
    assert 701 == titleToNumber(columnTitle), 'test 3'

    columnTitle = 'AZ'
    assert 52 == titleToNumber(columnTitle), 'test 4'
