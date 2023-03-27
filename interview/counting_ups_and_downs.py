from typing import List, Callable


def count_downs(s: str) -> int:
    res = 0
    level = 0
    prev = 0
    for item in s:
        if item == 'u':
            level += 1
        elif item == 'd':
            level -= 1
        else:
            return 0
        if level == 0 and prev < 0:
            res += 1
        prev = level
    return res


def test(f: Callable, testcase: List[tuple]) -> str:
    for test in testcase:
        assert test[0] == f(test[1])
    return 'all tests passed'


if __name__ == '__main__':
    testcase = [
        (1, 'ddduduuuu'),
        (2, 'duduuuu'),
        (3, 'uddududu'),
        (0, 'uuuuuu'),
        (0, ''),
        (0, 'mms'),
        (0, 'uuddmms'),
    ]
    print(test(count_downs, testcase))