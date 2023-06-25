def closeStrings(word1: str, word2: str) -> bool:
    w_1 = {}
    w_2 = {}
    for letter in word1:
        w_1[letter] = w_1.get(letter, 0) + 1
    for letter in word2:
        w_2[letter] = w_2.get(letter, 0) + 1

    if sorted(w_1.keys()) != sorted(w_2.keys()):
        return False

    if sorted(w_1.values()) != sorted(w_2.values()):
        return False
    return True


if __name__ == '__main__':
    word1 = "abc"
    word2 = "bca"
    assert True is closeStrings(word1, word2), 'test 1'

    word1 = "a"
    word2 = "aa"
    assert False is closeStrings(word1, word2), 'test 2'

    word1 = "cabbba"
    word2 = "abbccc"
    assert True is closeStrings(word1, word2), 'test 3'