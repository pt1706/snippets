def guess(num):
    if num == pick:
        return 0
    elif num > pick:
        return -1
    else:
        return 1


def guessNumber(n: int) -> int:
    l, r = 0, n
    while r > l:
        num = (r - l) // 2 + l
        pick = guess(num)
        if pick == 1:
            l = num + 1
        elif pick == -1:
            r = num - 1
        else:
            return num
    return l


if __name__ == '__main__':
    n = 10
    pick = 6
    assert pick == guessNumber(n), 'test 1'

    n = 2
    pick = 1
    assert pick == guessNumber(n), 'test 2'
