def numTilings(n: int) -> int:
    """still can't understand why this equation works"""
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 5
    r_prev_prev = 1
    r_prev = 2
    res = 5
    for i in range(4, n + 1):
        o_res = res
        res = res * 2 + r_prev_prev
        r_prev_prev = r_prev
        r_prev = o_res
    return res


if __name__ == '__main__':
    assert 1 == numTilings(1), 'test 1'
    assert 5 == numTilings(3), 'test 2'
    assert 11 == numTilings(4), 'test 3'
    assert 24 == numTilings(5), 'test 4'
    assert 53 == numTilings(6), 'test 5'
