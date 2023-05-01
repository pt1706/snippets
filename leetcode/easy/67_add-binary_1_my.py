def addBinary(a: str, b: str) -> str:
    diff = len(a) - len(b)
    if diff > 0:
        b = diff * '0' + b
    if diff < 0:
        a = -diff * '0' + a
    res = ''
    more = 0
    for digit in range(len(a) - 1, -1, -1):
        item = int(a[digit]) + int(b[digit]) + more
        if item == 2:
            more = 1
            item = 0
        elif item == 3:
            more = 1
            item = 1
        elif item < 2:
            more = 0
            item = item
        res = str(item) + res
    if more:
        res = str(more) + res
    return res


if __name__ == '__main__':
    a, b = '11', '1'
    assert '100' == addBinary(a, b)

    a, b = '11', '11'
    assert '110' == addBinary(a, b)

    a, b = '110', '100'
    assert '1010' == addBinary(a, b)

    a, b = '110', '110'
    assert '1100' == addBinary(a, b)

    a, b = '1010', '1011'
    assert '10101' == addBinary(a, b)
