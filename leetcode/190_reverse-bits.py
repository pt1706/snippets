def reverseBits(n: int) -> int:
    res = 0
    for i in range(32):
        bit = n & 1
        n = n >> 1
        res = res << 1
        res = res | bit
    return res


if __name__ == '__main__':
    n = 43261596
    assert 964176192 == reverseBits(n), 'test 1'

    n = 3221225471
    assert 4294967293 == reverseBits(n), 'test 2'
