import heapq


def reorganizeString(s: str) -> str:
    res = ''
    d = {}
    for i in s:
        d[i] = d.get(i, 0) - 1
    d = [(v, k) for k, v in d.items()]
    heapq.heapify(d)
    while d:
        n, first = heapq.heappop(d)
        if not res or res[-1] != first:
            res += first
            if n < -1:
                heapq.heappush(d, (n + 1, first))
            continue
        elif not d:
            return ''
        else:
            n_other, other = heapq.heappop(d)
            res += other
            if n_other < -1:
                heapq.heappush(d, (n_other + 1, other))
            if n <= -1:
                heapq.heappush(d, (n, first))
    return res


def reorganizeString_simple(s: str) -> str:
    """don't work with first digit"""
    l, r = 0, 1
    while l < len(s) - 2:
        while s[l] == s[r]:
            if r == len(s) - 1:
                return ""
            r += 1
        s = s[:l + 1] + s[r] + s[l + 1: r] + s[r + 1:]
        l += 1
        r = l + 1
    if s[l] == s[r]:
        return ""
    return s


if __name__ == '__main__':
    s = "aab"
    res = "aba"
    assert res == reorganizeString(s), 'test 1'

    s = "aaab"
    res = ""
    assert res == reorganizeString(s), 'test 2'

    s = "baaba"
    res = "ababa"
    assert res == reorganizeString(s), 'test 3'