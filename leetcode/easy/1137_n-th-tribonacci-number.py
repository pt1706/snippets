def tribonacci(n: int) -> int:
    c_1, c_2, c_3 = 0, 1, 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    for i in range(3, n + 1):
        c_1, c_2, c_3 = c_2, c_3, c_1 + c_2 + c_3
    return c_3


if __name__ == '__main__':
    assert 4 == tribonacci(4), 'test 1'
