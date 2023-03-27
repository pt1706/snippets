def isValid(s: str) -> bool:
    chars = ['()', '[]', '{}']
    while True:
        lengh = len(s)
        for char in chars:
            lst = s.split(char)
            s = ''.join(lst)
        if lengh == len(s):
            return False
        elif len(s) == 0:
            return True


def isValid_1(s: str) -> bool:
    stack = []
    opening = set('([{')
    closing = set(')]}')
    pair = {')': '(', ']': '[', '}': '{'}
    for i in s:
        if i in opening:
            stack.append(i)
        if i in closing:
            if not stack:
                return False
            elif stack.pop() != pair[i]:
                return False
            else:
                continue
    if not stack:
        return True
    else:
        return False


if __name__ == '__main__':
    assert True is isValid("()")
    assert True is isValid("()[]{}")
    assert False is isValid("(]")
    assert False is isValid("([)]")
    assert False is isValid("[])(")
    assert False is isValid("(}{)")
    assert True is isValid("{[]}")

    assert True is isValid_1("()")
    assert True is isValid_1("()[]{}")
    assert False is isValid_1("(]")
    assert False is isValid_1("([)]")
    assert False is isValid_1("[])(")
    assert False is isValid_1("(}{)")
    assert True is isValid_1("{[]}")
