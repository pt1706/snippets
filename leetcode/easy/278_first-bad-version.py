def firstBadVersion(n: int) -> int:
    l = 1
    h = n
    while h - l > 1:
        m = (h + l) // 2
        if isBadVersion(m):
            h = m
        else:
            l = m
    if isBadVersion(l):
        return l
    return h