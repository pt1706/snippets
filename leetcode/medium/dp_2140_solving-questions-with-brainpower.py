from typing import List


def mostPoints(questions: List[List[int]]) -> int:
    dp = {}
    for i in range(len(questions) - 1, -1, -1):
        dp[i] = max((questions[i][0]) + dp.get(questions[i][1] + i + 1, 0), dp.get(i + 1, 0))
    return dp[0]


def mostPoints_cash(questions: List[List[int]]) -> int:
    dp = {}
    def dfs(i):
        if i >= len(questions):
            return 0
        if i in dp:
            return dp[i]
        dp[i] = max((questions[i][0] + dfs(i + 1 + questions[i][1]), dfs(i + 1)))
        return dp[i]

    return dfs(0)


def mostPoints_my_cash(questions: List[List[int]]) -> int:
    dp = {}
    questions = tuple((x, y) for x, y in questions)

    def dfs(questions, res):
        if not questions:
            return res
        n_q = tuple(questions[questions[0][1] + 1:])
        new_res = res + questions[0][0]
        n = (n_q, new_res)
        c = (questions[1:], res)
        if not dp.get(c):
            dp[c] = dfs(questions[1:], res)
        if not dp.get(n):
            dp[n] = dfs(n_q, new_res)

        return max(dp[c], dp[n])

    return dfs(questions, 0)


def mostPoints_rec(questions: List[List[int]]) -> int:
    def dfs(questions, res):
        if not questions:
            return res
        n_q = questions[questions[0][1] + 1:]
        new_res = res + questions[0][0]
        return max(dfs(questions[1:], res), dfs(n_q, new_res))

    return dfs(questions, 0)


if __name__ == '__main__':
    questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
    assert 5 == mostPoints(questions), 'test 1'

    questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    assert 7 == mostPoints(questions), 'test 2'

    questions = [[43, 5]]
    assert 43 == mostPoints(questions), 'test 3'