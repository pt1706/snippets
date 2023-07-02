def minFlips(a: int, b: int, c: int) -> int:
    res = 0
    while c or b or a:
        bit_c = c & 1
        bit_a = a & 1
        bit_b = b & 1
        if bit_c == 1 and bit_a == 0 and bit_b == 0:
            res += 1
        elif bit_c == 0 and bit_a == 1 and bit_b == 1:
            res += 2
        elif bit_c == 0 and (bit_a or bit_b) == 1:
            res += 1
        c = c >> 1
        a = a >> 1
        b = b >> 1
    return res


if __name__ == '__main__':
    a = 2
    b = 6
    c = 5
    assert 3 == minFlips(a, b, c), 'test 1'

    a = 4
    b = 2
    c = 7
    assert 1 == minFlips(a, b, c), 'test 2'

    a = 1
    b = 2
    c = 3
    assert 0 == minFlips(a, b, c), 'test 3'

    a = 8
    b = 3
    c = 5
    assert 3 == minFlips(a, b, c), 'test 4'
