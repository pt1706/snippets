def addBinary(a: str, b: str) -> str:
    res = ''
    carry = 0
    a, b = a[::-1], b[::-1]

    for i in range(max(len(a), len(b))):
        digitA = a[i] if i < len(a) else 0
        digitB = b[i] if i < len(b) else 0

        total = int(digitA) + int(digitB) + carry
        char = str(total % 2)
        res = char + res
        carry = total // 2

    if carry:
        res = '1' + res
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
