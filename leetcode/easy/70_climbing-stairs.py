import time


def timing(f):
    def wrapper(*args):
        start = time.time()
        res = f(*args)
        print(f'time of exuction: {(time.time() - start):9.6f} s\n')
        return res
    return wrapper


def climbStairs(n: int) -> int:
    res = 1
    prev = 1
    for i in range(1, n):
        current = res
        res = res + prev
        prev = current
    return res


def climbStairs_long(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs_long(n - 1) + climbStairs_long(n - 2)


def climbStairs_with_cash(n: int) -> int:
    d = {}
    def dfs(cur):
        if cur > n:
            return 0
        if cur == n:
            return 1
        cur_1 = d.get(cur + 1)
        cur_2 = d.get(cur + 2)
        if not cur_1:
            cur_1 = dfs(cur + 1)
            d[cur + 1] = cur_1
        if not cur_2:
            cur_2 = dfs(cur + 2)
            d[cur + 2] = cur_2
        return cur_1 + cur_2
    return dfs(0)


@timing
def test(f, testcases):
    for case in testcases:
        assert case[0] == f(case[1])
    print('all tests passed')


@timing
def test_1(f, arg):
    return f(arg)


if __name__ == '__main__':
    testcases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (5, 4),
        (8, 5),
        (987, 15)
    ]
    test(climbStairs, testcases)
    test(climbStairs_long, testcases)
    test(climbStairs_with_cash, testcases)

    print(test_1(climbStairs, 38))
    print(test_1(climbStairs_long, 38))
