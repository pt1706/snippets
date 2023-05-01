def mergeAlternately(word1: str, word2: str) -> str:
    res = ''
    for i in range(min(len(word1), len(word2))):
        res += word1[i] if i < len(word1) else ''
        res += word2[i] if i < len(word2) else ''
    res += word1[i + 1:] if i + 1 < len(word1) else ''
    res += word2[i + 1:] if i + 1 < len(word2) else ''
    return res


if __name__ == '__main__':
    word1 = 'abc'
    word2 = 'pqr'
    res = 'apbqcr'
    assert res == mergeAlternately(word1, word2), 'test 1'

    word1 = 'ab'
    word2 = 'pqrs'
    res = 'apbqrs'
    assert res == mergeAlternately(word1, word2), 'test 2'

    word1 = 'abcd'
    word2 = 'pq'
    res = 'apbqcd'
    assert res == mergeAlternately(word1, word2), 'test 3'