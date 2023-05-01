def addBinary(a: str, b: str) -> str:
    res = 0
    for item in (a, b):
        res += int('0b' + item, 2)
    res = str(bin(res)).split('b')
    return str(res[1])


if __name__ == '__main__':
    a, b = '11', '1'
    assert '100' == addBinary(a, b)

    a, b = '111', '10'
    assert '1001' == addBinary(a, b)

    a, b = '11', '11'
    assert '110' == addBinary(a, b)

    a, b = '110', '100'
    assert '1010' == addBinary(a, b)

    a, b = '110', '110'
    assert '1100' == addBinary(a, b)

    a, b = '1010', '1011'
    assert '10101' == addBinary(a, b)
