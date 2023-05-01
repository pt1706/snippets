import string


def isPalindrome(s: str) -> bool:
    def is_num_or_al(char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))

    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not is_num_or_al(s[l]):
            l += 1
        while l < r and not is_num_or_al(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def isPalindrome_1(s: str) -> bool:
    if not s:
        return True
    s = [x.lower() for x in s if x.isalnum()]
    print(s)
    return s == s[::-1]


ascii = string.ascii_lowercase
numbers = string.digits


def isPalindrome_2(s: str) -> bool:
    if not s:
        return True
    s = s.lower().split()
    s = ''.join(s)
    s = [x for x in s if x in numbers or x in ascii]
    s = ''.join(s)
    return s == s[::-1]


if __name__ == '__main__':
    s = 'A man, a plan, a canal: Panama'
    assert True is isPalindrome(s)

    s = 'race a car'
    assert False is isPalindrome(s)

    s = ''
    assert True is isPalindrome(s)