def strStr(haystack: str, needle: str) -> int:
    lst = haystack.split(needle)
    if len(lst[0]) == len(haystack):
        return -1
    return len(lst[0])


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    assert 0 == strStr(haystack, needle)
    haystack = "leetcode"
    needle = "leeto"
    assert -1 == strStr(haystack, needle)
    haystack = "basadbutsad"
    needle = "sad"
    assert 2 == strStr(haystack, needle)