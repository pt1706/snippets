from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort()
    res = 0
    prev_end = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prev_end:
            prev_end = end
        else:
            res += 1
            prev_end = min(end, prev_end)
    return res


def eraseOverlapIntervals_my(intervals: List[List[int]]) -> int:
    count = 0
    n = len(intervals)
    res = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        l_r, r_r = intervals[r]
        for c in range(n):
            l_c, r_c = intervals[c]
            if (l_r < l_c and r_r <= l_c) or (l_c < l_r and r_c <= l_r):
                res[r][c] = 0
            else:
                res[r][c] = 1
    while True:
        i_int = 0
        intersec = 1
        for i in range(len(res)):
            if intersec < sum(res[i]):
                i_int = i
                intersec = sum(res[i])
        if intersec > 1:
            count += 1
            deleted = res[i_int]
            res[i_int] = [0 for _ in range(n)]
            for c in range(len(deleted)):
                if deleted[c] == 1:
                    res[c][i_int] = 0
        else:
            return count


if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    assert 1 == eraseOverlapIntervals(intervals), 'test 1'

    intervals = [[1, 2], [1, 2], [1, 2]]
    assert 2 == eraseOverlapIntervals(intervals), 'test 2'

    intervals = [[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]]
    assert 4 == eraseOverlapIntervals(intervals), 'test 3'
