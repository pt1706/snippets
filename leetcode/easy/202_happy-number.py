def isHappy(n: int) -> bool:
    visited = [n]
    while n != 1:
        s = str(n)
        n = 0
        for digit in s:
            n += int(digit)**2
        if n in visited:
            return False
        visited.append(n)
    return True


if __name__ == '__main__':
    n = 19
    assert True is isHappy(n), 'test 1'

    n = 2
    assert False is isHappy(n), 'test 2'