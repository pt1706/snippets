def check_palindrome(string: str) -> bool:
    return string == string[::-1]


def check_palindrome_2(string: str) -> bool:
    return string == ''.join(string[x] for x in range(len(string) - 1, -1, -1))


def check_palindrome_3(string: str) -> bool:
    return string == ''.join(string[x] for x in reversed(range(len(string))))


def test(f):
    cases = dict(
        [
            ('abccba', True),
            ('abcdecba', False),
            ('abcddcba', True),
            ('ab cddcba', False),
        ]
    )
    for (string, res) in cases.items():
        # print(f'expected - {res}; actual {f(string)}')
        assert res is f(string)
    print('all test done')


if __name__ == '__main__':
    test(check_palindrome_3)