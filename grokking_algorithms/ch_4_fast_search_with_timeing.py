import time
import random


def quiq_sort_pivot_center(lst):
    if len(lst) < 2:
        return lst
    if len(lst) == 2:
        return [lst[0], lst[1]] if lst[0] <= lst[1] else [lst[1], lst[0]]
    pivot = lst.pop(len(lst) // 2)
    big = []
    less = []
    for i in lst:
        if i >= pivot:
            big += [i]
        else:
            less += [i]
    return quiq_sort_pivot_center(less) + [pivot] + quiq_sort_pivot_center(big)


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


def conv_search(lst):
    res = []
    while lst:
        small = 100000000
        small_index = 0
        for i in range(len(lst)):
            if lst[i] < small:
                small = lst[i]
                small_index = i
        res += [lst.pop(small_index)]
    return res


if __name__ == "__main__":
    lst = [random.randrange(-100, 100) for i in range(10000)]
    lst1 = [random.randrange(-100, 100) for i in range(10000)]
    lst2 = [random.randrange(-100, 100) for i in range(10000)]

    for lst in [lst, lst1, lst2]:
        print('Test')
        start_time = time.time()
        res = quiq_sort(lst)
        time_operation = (time.time() - start_time)
        print("---%s takes: %07.3f ms ---" %
              (quiq_sort.__name__, time_operation * 1000))

        start_time = time.time()
        res = sorted(lst)
        time_operation = (time.time() - start_time)
        print("---%s takes: %07.3f ms ---" %
              (sorted.__name__, time_operation * 1000))

        start_time = time.time()
        res = conv_search(lst)
        time_operation = (time.time() - start_time)
        print("---%s takes: %07.3f ms ---" %
              (conv_search.__name__, time_operation * 1000))
        print()
