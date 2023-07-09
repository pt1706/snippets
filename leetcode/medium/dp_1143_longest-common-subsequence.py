def longestCommonSubsequence(text1: str, text2: str) -> int:
    row = len(text2)
    col = len(text1)
    res = [[0 for c in range(col + 1)] for r in range(row + 1)]
    for r in range(1, row + 1):
        for c in range(1, col + 1):
            item = 0
            if text2[r - 1] == text1[c - 1]:
                item = 1
            res[r][c] = max(res[r - 1][c - 1] + item, res[r][c - 1], res[r - 1][c])
    return res[row][col]


if __name__ == '__main__':
    text1 = 'abcde'
    text2 = 'ace'
    assert 3 == longestCommonSubsequence(text1, text2), 'test 1'

    text1 = 'abc'
    text2 = 'abc'
    assert 3 == longestCommonSubsequence(text1, text2), 'test 2'

    text1 = 'abc'
    text2 = 'def'
    assert 0 == longestCommonSubsequence(text1, text2), 'test 3'