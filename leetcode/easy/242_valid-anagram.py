from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    d_s, d_t = {}, {}

    for i in range(len(s)):
        d_s[s[i]] = 1 + d_s.get(s[i], 0)
        d_t[t[i]] = 1 + d_t.get(t[i], 0)

    for j in d_s:
        if d_s[j] != d_t.get(j, 0):
            return False
    return True


def isAnagram_2(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


def isAnagram_1(s: str, t: str) -> bool:
    s, t = sorted(s), sorted(t)
    return s == t


if __name__ == '__main__':
    s = 'anagram'
    t = 'nagaram'
    assert True is isAnagram(s, t), 'test 1'

    s = 'rat'
    t = 'cat'
    assert False is isAnagram(s, t), 'test 2'
