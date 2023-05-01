from typing import List


def generate(numRows: int) -> List[List[int]]:
    res = []
    for i in range(numRows):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(res[i - 1][j] + res[i - 1][j - 1])
        res.append(row)
    return res


if __name__ == '__main__':
    res = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert res == generate(5)

    res = [[1]]
    assert res == generate(1)
