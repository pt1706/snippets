def reverse(x: int) -> int:
    mn = -2 ** 31
    mx = 2 ** 31 - 1

    if x > 0:
        s = 1
    else:
        s = -1
    res = 0
    x = abs(x)

    while x:

        item = x % 10
        if x > 0 and (res > mx // 10 or (res == mx // 10 and item > mx % 10)):
            return 0
        if x < 0 and (res > abs(mn) // 10 or (res == abs(mn) // 10 and item > abs(mn) % 10)):
            return 0
        x = x // 10
        res *= 10
        res += item

    return res * s


if __name__ == '__main__':
    x = -2147483412
    assert -2143847412 == reverse(x), 'test 1'
