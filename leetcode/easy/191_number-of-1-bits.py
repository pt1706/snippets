def hammingWeight(n: int) -> int:
    res = 0
    while n:
        if n & 1:   # or n % 2 or instead if: res += n & 1
            res += 1
        n = n >> 1
    return res


if __name__ == '__main__':
    n = 11
    assert 3 == hammingWeight(n), 'test 1'

    n = 128
    assert 1 == hammingWeight(n), 'test 2'

    n = 4294967293
    assert 31 == hammingWeight(n), 'test 2'