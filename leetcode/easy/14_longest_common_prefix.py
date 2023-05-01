from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    index = 0
    strs = sorted(strs, key=len)
    while index <= len(strs[0]) - 1:
        for word in strs[1:]:
            if strs[0][index] != word[index]:
                return strs[0][:index]
        index += 1
    return strs[0]


def longestCommonPrefix_1(strs: List[str]) -> str:
    strs = sorted(strs, key=len, reverse=True)
    word = strs.pop()
    while len(word) > 0:
        if all(map(lambda item: word == item[:len(word)], strs)):
            return word
        word = word[:-1]
    return ''


if __name__ == '__main__':
    assert "fl" == longestCommonPrefix(["flower", "flow", "flight"])
    assert "" == longestCommonPrefix(["dog", "racecar", "car"])
    assert "a" == longestCommonPrefix(["ab", "a"])

    assert "fl" == longestCommonPrefix_1(["flower", "flow", "flight"])
    assert "" == longestCommonPrefix_1(["dog", "racecar", "car"])
    assert "a" == longestCommonPrefix_1(["ab", "a"])