# ------------------quick search-----------------------------------


def quiq_sort(lst):
    if len(lst) < 2:
        return lst
    if len(lst) == 2:
        return [lst[0], lst[1]] if lst[0] <= lst[1] else [lst[1], lst[0]]
    pivot = lst.pop()
    big = []
    less = []
    for i in lst:
        if i >= pivot:
            big += [i]
        else:
            less += [i]
    return quiq_sort(less) + [pivot] + quiq_sort(big)


if __name__ == "__main__":
    assert quiq_sort([90, 1, 12, 2, 0, 4]) == [0, 1, 2, 4, 12, 90]
    assert quiq_sort([68, 19, 11, -69, 34, -12, -58, 10, -87, 41]) == [
        -87, -69, -58, -12, 10, 11, 19, 34, 41, 68
    ]
    import random

    lst = [random.randrange(-100, 100) for i in range(10)]
    s_lst = sorted(lst)
    assert quiq_sort(lst) == s_lst
    lst = [random.randrange(-100, 100) for i in range(10)]
    s_lst = sorted(lst)
    assert quiq_sort(lst) == s_lst
    print('all tests passed')


# ------------------2 exercice-----------------------------------


def my_sum(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + my_sum(lst[1:])


if __name__ == "__main__":
    test_list = [90, 1, 12, 2, 0, 4]
    assert my_sum(test_list) == 109

# ------------------3 exercice-----------------------------------


def my_big(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] if lst[0] > my_big(lst[1:]) else my_big(lst[1:])


if __name__ == "__main__":
    test_list = [90, 1, 12, 2, 0, 4]
    assert my_big(test_list) == 90
    test_list = [90, 1, 12, 2, 0, 109, 4]
    assert my_big(test_list) == 109
