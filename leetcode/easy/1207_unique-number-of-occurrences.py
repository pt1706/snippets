from typing import List


def uniqueOccurrences(arr: List[int]) -> bool:
    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1
    return len(d.values()) == len(set(d.values()))


if __name__ == '__main__':
    arr = [1, 2, 2, 1, 1, 3]
    assert True is uniqueOccurrences(arr), 'test 1'

    arr = [1, 2]
    assert False is uniqueOccurrences(arr), 'test 2'

    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    assert True is uniqueOccurrences(arr), 'test 3'
