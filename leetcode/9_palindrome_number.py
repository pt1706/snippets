def is_palindrome(x: int) -> bool:
    string = str(x)
    palindrome = string[::-1]
    return string == palindrome


def is_palindrome_non_str(x: int) -> bool:
    initial = abs(x)
    res = 0
    y = 0
    while x > 0:
        y = x % 10
        x = x // 10
        res = res * 10 + y
    return initial == res


if __name__ == '__main__':
    assert True is is_palindrome(24566542)
    assert True is is_palindrome_non_str(24566542)
    assert False is is_palindrome_non_str(-24566542)
