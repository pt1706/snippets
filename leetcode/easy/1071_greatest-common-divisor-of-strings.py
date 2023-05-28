

def gcdOfStrings(str1: str, str2: str) -> str:
    def sub(s, target):
        while target:
            if s != target[:len(s)]:
                return False
            target = target[len(s):]
        return True

    s = str1 if len(str1) <= len(str2) else str2
    target = str2 if len(str1) <= len(str2) else str1
    for i in range(len(s)):
        if sub(s[i:], s):
            if sub(s[i:], target):
                return s[i:]
    return ''


if __name__ == '__main__':
    str1 = 'ABCABC'
    str2 = 'ABC'
    res = 'ABC'
    assert res == gcdOfStrings(str1, str2), 'test 1'

    str1 = 'ABABAB'
    str2 = 'ABAB'
    res = 'AB'
    assert res == gcdOfStrings(str1, str2), 'test 2'

    str1 = 'LEET'
    str2 = 'CODE'
    res = ''
    assert res == gcdOfStrings(str1, str2), 'test 3'