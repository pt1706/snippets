from typing import List


def minCost(n: int, cuts: List[int]) -> int:
    d = {}

    def cut(l, r):
        if r - l == 1:
            return 0
        if (l, r) in d:
            return d[(l, r)]

        res = float('inf')
        for i in cuts:
            if l < i < r:
                res = min(res, (r - l + cut(l, i) + cut(i, r)))
        d[(l, r)] = 0 if res == float('inf') else res

        return d[(l, r)]

    cuts.sort()
    return cut(0, n)


def minCost_my(n: int, cuts: List[int]) -> int:
    def cut(n, cuts):
        if len(cuts) == 1:
            return n
        c = cuts[len(cuts) // 2]
        c_1 = cuts[0:len(cuts) // 2]
        c_2 = cuts[len(cuts) // 2 + 1:]
        c_2 = [i - c for i in c_2]
        f = cut(c, c_1) if c_1 else 0
        s = cut(n - c, c_2) if c_2 else 0
        res = n + f + s
        if len(cuts) % 2 == 0:
            c = cuts[len(cuts) // 2 - 1]
            c_1 = cuts[0:len(cuts) // 2 - 1]
            c_2 = cuts[len(cuts) // 2:]
            c_2 = [i - c for i in c_2]
            f = cut(c, c_1) if c_1 else 0
            s = cut(n - c, c_2) if c_2 else 0
            res_1 = n + f + s
            res = min(res, res_1)
        return res

    cuts.sort()
    return cut(n, cuts)


if __name__ == '__main__':
    n = 7
    cuts = [1, 3, 4, 5]
    assert 16 == minCost(n, cuts), 'test 1'

    n = 9
    cuts = [5, 6, 1, 4, 2]
    assert 22 == minCost(n, cuts), 'test 2'

    n = 20
    cuts = [13, 6, 7, 2, 10]
    assert 50 == minCost(n, cuts), 'test 3'