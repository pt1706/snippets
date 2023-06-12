from typing import List


def decodeString(s: str) -> str:
    def helper(s: str) -> List[str]:
        i = 0
        res = ''
        while s and i < len(s):
            if s[i].isnumeric():
                j = i + 1
                while s[j] != '[':
                    j += 1
                out = helper(s[j + 1:])
                res += int(s[i:j]) * out[0]
                s = out[1]
                i = 0
                continue
            if s[i] == ']':
                return [res, s[i + 1:]]
            res += s[i]
            i += 1
        return [res, '']

    return helper(s)[0]


if __name__ == '__main__':
    s = '3[a]2[bc]'
    res = 'aaabcbc'
    assert res == decodeString(s), 'test 1'

    s = '3[a2[c]]'
    res = 'accaccacc'
    assert res == decodeString(s), 'test 2'

    s = '2[abc]3[cd]ef'
    res = 'abcabccdcdcdef'
    assert res == decodeString(s), 'test 3'

    s = '11[leetcode]'
    res = 'leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode'
    assert res == decodeString(s), 'test 4'
