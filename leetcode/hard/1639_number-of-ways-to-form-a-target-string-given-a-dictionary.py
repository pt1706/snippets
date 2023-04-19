from collections import defaultdict
from typing import List


def numWays(words: List[str], target: str) -> int:
    d = defaultdict(int)
    for w in words:
        for (i, c) in enumerate(w):
            d[(i, c)] += 1
    dp = {}

    def dfs(index, target):
        if len(target) > len(words[0]) - index:
            return 0
        qty = d[index, target[0]]
        if len(target) == 1:
            if index + 1 == len(d):
                return qty
            else:
                if (index + 1, target) not in dp:
                    dp[(index + 1, target)] = dfs(index + 1, target)
                return qty + dp[(index + 1, target)]
        if (index + 1, target) not in dp:
            dp[(index + 1, target)] = dfs(index + 1, target)
        if (index + 1, target[1:]) not in dp:
            dp[(index + 1, target[1:])] = dfs(index + 1, target[1:])

        return dp[(index + 1, target)] + qty * dp[(index + 1, target[1:])]

    return dfs(0, target)


def numWays_without_cash(words: List[str], target: str) -> int:
    d = defaultdict(int)
    for w in words:
        for (i, c) in enumerate(w):
            d[(i, c)] += 1

    def dfs(index, target):
        if len(target) > len(words[0]) - index:
            return 0
        qty = d[index, target[0]]
        if len(target) == 1:
            if index + 1 == len(d):
                return qty
            else:
                return qty + dfs(index + 1, target)
        return dfs(index + 1, target) + qty * dfs(index + 1, target[1:])
    return dfs(0, target)


if __name__ == '__main__':
    # words = ["acca", "bbbb", "caca"]
    # target = "aba"
    # print(numWays(words, target))

    words = ["acca", "bbbb", "caca"]
    target = "aba"
    assert 6 == numWays(words, target), 'test 1'

    words = ["abba", "baab"]
    target = "bab"
    assert 4 == numWays(words, target), 'test 2'