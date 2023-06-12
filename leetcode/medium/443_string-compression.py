from typing import List


def compress(chars: List[str]) -> int:
    i, l, r = 0, 0, 1
    while l < len(chars):
        while r < len(chars) and chars[l] == chars[r]:
            r += 1
        chars[i] = chars[l]
        if r - l > 1:
            for j in str(r - l):
                i += 1
                chars[i] = j
        i += 1
        l = r
        r += 1
    return i


if __name__ == '__main__':
    chars = ["a"]
    assert 1 == compress(chars), 'test 1.1'
    assert chars[:1] == ["a"], 'test 1.2'

    chars = ["a", "a", "b", "b", "c", "c", "c"]
    assert 6 == compress(chars), 'test 2.1'
    assert chars[:6] == ["a", "2", "b", "2", "c", "3"], 'test 2.2'

    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    assert 4 == compress(chars), 'test 3.1'
    assert chars[:4] == ["a", "b", "1", "2"], 'test 3.2'

    chars = ["a", "b", "c"]
    assert 3 == compress(chars), 'test 4.1'
    assert chars[:3] == ["a", "b", "c"], 'test 4.2'
