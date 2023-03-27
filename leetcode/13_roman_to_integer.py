alphabet = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def romanToInt(s: str) -> int:
    res = 0
    previous = 0
    for item in s:
        if alphabet[item] <= previous:
            res += alphabet[item]
        else:
            res += alphabet[item] - 2 * previous
        previous = alphabet[item]
    return res


if __name__ == '__main__':
    assert 1004 == romanToInt("MIV")
    assert 3 == romanToInt("III")
    assert 1994 == romanToInt("MCMXCIV")
