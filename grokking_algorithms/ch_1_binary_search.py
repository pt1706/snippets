def binary_search(test_set, item):
    middle = len(test_set) // 2
    length = len(test_set)
    while True:
        mid_value = test_set[middle]
        if item == mid_value:
            return middle
        if item < mid_value:
            length = middle
            middle = middle // 2
        else:
            middle += (length - middle) // 2


if __name__ == "__main__":
    test_set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert binary_search(test_set, 13) == 13
    assert binary_search(test_set, 9) == 9
    assert binary_search(test_set, 6) == 6
    assert binary_search(test_set, 14) == 14
    assert binary_search(test_set, 0) == 0
    print('all tests passed')


def binary_search(test_set, item):
    low = 0
    high = len(test_set) - 1
    while low <= high:
        mid = (high + low) // 2
        if item == test_set[mid]:
            return mid
        if item < test_set[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    test_set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print(binary_search(test_set, 13))
    assert binary_search(test_set, 13) == 13
    assert binary_search(test_set, 9) == 9
    assert binary_search(test_set, 6) == 6
    assert binary_search(test_set, 14) == 14
    assert binary_search(test_set, 0) == 0
    assert binary_search(test_set, -1) is None
    assert binary_search(test_set, 15) is None
    print('all tests passed')
