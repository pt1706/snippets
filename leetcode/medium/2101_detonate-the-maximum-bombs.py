from collections import deque
from typing import List


def maximumDetonation(bombs: List[List[int]]) -> int:
    def helper(b):
        det = [b]
        q = deque()
        q.append(b)
        while q and len(det) <= len(bombs):
            x, y, r = bombs[q.popleft()]
            for i in range(len(bombs)):
                if i not in det:
                    x_i, y_i, r_i = bombs[i]
                    distance = ((x - x_i) ** 2 + (y - y_i) ** 2) ** .5
                    if distance <= r:
                        det.append(i)
                        q.append(i)
        return len(det)

    res = 0
    for i in range(len(bombs)):
        res = max(res, helper(i))
    return res


if __name__ == '__main__':
    bombs = [[2, 1, 3], [6, 1, 4]]
    assert 2 == maximumDetonation(bombs), 'test 1'