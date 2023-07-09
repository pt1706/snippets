from typing import List


def combinationSum3(k: int, n: int) -> List[List[int]]:
    result = []

    def dfs(res, n, k):
        nonlocal result
        if not res:
            last = 0
        else:
            last = res[-1]

        for i in range(last + 1, 10):
            n_res = res[:]
            n_res.append(i)
            if n - i == 0 and k == 0:
                result.append(n_res)
            if n - i > 0 and k > 0:
                dfs(n_res, n - i, k - 1)

    dfs([], n, k - 1)
    return result


if __name__ == '__main__':
    res = [[1, 2, 4]]
    assert res == combinationSum3(3, 7), 'test 1'

    res = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert res == combinationSum3(9, 45), 'test 2'
