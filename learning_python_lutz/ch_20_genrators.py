def get_seq(n):
    a, b, c = 1, 1, 1

    for i in range(n):
        if i < 3:
            res = 1
        else:
            res = a + b + c
            a = b
            b = c
            c = res
        yield res


if __name__ == '__main__':
    assert list(get_seq(7)) == [1, 1, 1, 3, 5, 9, 17]
    assert list(get_seq(6)) == [1, 1, 1, 3, 5, 9]
    assert list(get_seq(8)) == [1, 1, 1, 3, 5, 9, 17, 31]
    print('all tests passed')
