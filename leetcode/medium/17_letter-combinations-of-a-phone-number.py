from typing import List


def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = []

    def dfs(i, subres):
        if i >= len(digits) and subres not in res:
            res.append(subres)
            return
        for j in d[digits[i]]:
            dfs(i + 1, subres + j)

    dfs(0, '')
    return res


if __name__ == '__main__':
    digits = "23"
    res = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert res == letterCombinations(digits), 'test 1'

    digits = ''
    res = []
    assert res == letterCombinations(digits), 'test 2'

    digits = "2"
    res = ['a', 'b', 'c']
    assert res == letterCombinations(digits), 'test 3'
