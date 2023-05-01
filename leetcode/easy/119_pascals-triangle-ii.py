from typing import List


def getRow(rowIndex: int) -> List[int]:
    row = []
    res = []
    for i in range(rowIndex + 1):
        for j in range(i + 1):
            if j == 0 or j == i:
                item = 1
            else:
                item = res[i - 1][j - 1] + res[i - 1][j]
            row.append(item)
        res.append(row)
        row = []
    return res[-1]


if __name__ == '__main__':
    res = [1, 4, 6, 4, 1]
    assert res == getRow(4)

    res = [1, 3, 3, 1]
    assert res == getRow(3)

    res = [1]
    assert res == getRow(0)