def characterReplacement(s: str, k: int) -> int:
    res = 0
    l = 0
    r = 1
    d = {s[0]: 1}
    while r < len(s):
        d[s[r]] = d.get(s[r], 0) + 1
        max_val = max(d.values())
        if r - l + 1 - max_val <= k:
            res = max(res, r - l + 1)
        else:
            d[s[l]] -= 1
            l += 1
        r += 1
    return res


def characterReplacement_optimized(s: str, k: int) -> int:
    res = 0
    l = 0
    r = 1
    d = {s[0]: 1}
    max_val = 0
    while r < len(s):
        d[s[r]] = d.get(s[r], 0) + 1
        max_val = max(max_val, d.get(s[r]))
        if r - l + 1 - max_val <= k:
            res = max(res, r - l + 1)
        else:
            d[s[l]] -= 1
            l += 1
        r += 1
    return res


def characterReplacement_my(s: str, k: int) -> int:
    """don't work with BAAAB"""
    res = 0
    for i in range(len(s)):
        if i == 0 or s[i] != s[i - 1]:
            tmp = k
            j = i + 1
            while j < len(s):
                if s[j] != s[i]:
                    if not tmp:
                        break
                    tmp -= 1
                res = max(res, j - i)
                j += 1
    for i in range(len(s) - 1, -1, -1):
        if i == len(s) - 1 or s[i] != s[i + 1]:
            tmp = k
            j = i - 1
            while j >= 0:
                if s[j] != s[i]:
                    if not tmp:
                        break
                    tmp -= 1
                res = max(res, i - j)
                j -= 1
    return res + 1


if __name__ == '__main__':
    s = "ABAB"
    k = 2
    assert 4 == characterReplacement(s, k), 'test 1'

    s = "AABABBA"
    k = 1
    assert 4 == characterReplacement(s, k), 'test 2'