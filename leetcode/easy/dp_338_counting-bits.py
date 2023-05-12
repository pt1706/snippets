from typing import List


def countBits(n: int) -> List[int]:
    res = [0]
    p = 1
    for i in range(1, n + 1):
        if i == p * 2:
            p = i
        res.append(1 + res[i - p])
    return res


if __name__ == '__main__':
    n = 2
    assert [0, 1, 1] == countBits(n), 'test 1'

    n = 5
    assert [0, 1, 1, 2, 1, 2] == countBits(n), 'test 1'
