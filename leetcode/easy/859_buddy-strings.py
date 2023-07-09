def buddyStrings(s: str, goal: str) -> bool:
    if len(goal) != len(s):
        return False
    if s == goal:
        let = []
        for i in s:
            if i in let:
                return True
            let.append(i)

    dif = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            dif.append(i)

    if len(dif) != 2:
        return False

    i, j = dif
    if s[i] == goal[j] and s[j] == goal[i]:
        return True
    return False


def buddyStrings_simple(s: str, goal: str) -> bool:
    if len(goal) != len(s):
        return False
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[:i] + s[j] + s[i + 1: j] + s[i] + s[j + 1:] == goal:
                return True
    return False


if __name__ == '__main__':
    s = "ab"
    goal = "ba"
    assert True is buddyStrings(s, goal), 'test 1'

    s = "abcd"
    goal = "cbad"
    assert True is buddyStrings(s, goal), 'test 2'

    s = "ab"
    goal = "ab"
    assert False is buddyStrings(s, goal), 'test 3'

    s = "aa"
    goal = "aa"
    assert True is buddyStrings(s, goal), 'test 4'
