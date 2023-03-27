def search_small(lst, exist=[]):
    smallest = 10000000
    for i in lst[:]:
        if i < smallest and i not in exist:
            smallest = i
    return smallest


def sorting(lst):
    res = []
    while len(lst) != len(res):
        item = search_small(lst, res)
        res += [item]
    return res


if __name__ == "__main__":
    test_lis = [90, -1, 12, 127, 0, 9, -12, 15, 7, 21, 100, 99, -98, -15]
    assert sorting(test_lis) == [
        -98, -15, -12, -1, 0, 7, 9, 12, 15, 21, 90, 99, 100, 127
    ]

# ------------------2 exercice-----------------------------------


def search_small_index(lst):
    smallest = lst[0]
    small_index = 0
    for i in range(1, len(lst)):
        if lst[i] < smallest:
            small_index = i
            smallest = lst[i]
    return small_index


def sorting(lst):
    res = []
    while lst:
        index = search_small_index(lst)
        res += [lst.pop(index)]
    return res


if __name__ == "__main__":
    test_list = [90, -1, 12, 127, 0, 9, -12, 15, 7, 21, 100, 99, -98, -15]
    assert sorting(test_list) == [
        -98, -15, -12, -1, 0, 7, 9, 12, 15, 21, 90, 99, 100, 127
    ]
