from typing import List


def makeArrayIncreasing(arr1: List[int], arr2: List[int]) -> int:
    tmp = arr1[:]
    arr2 = list(set(arr2))
    r = 0
    res = 0
    for l in range(len(arr1)):
        if (l < len(arr1) - 1 and arr1[l] >= arr1[l + 1]) or (l > 0 and arr1[l] <= arr1[l - 1]):
            while r < len(arr2):
                if arr2[r] > arr1[l - 1]:
                    arr1[l] = arr2[r]
                    res += 1
                    break
                r += 1
            else:
                res = -1
                break
    if res != -1:
        return res
    arr1 = tmp[:]
    res = 0
    r = 0
    arr1[0] = arr2[0]
    for l in range(len(arr1)):
        if (l < len(arr1) - 1 and arr1[l] >= arr1[l + 1]) or (l > 0 and arr1[l] <= arr1[l - 1]):
            while r < len(arr2):
                if arr2[r] > arr1[l - 1]:
                    arr1[l] = arr2[r]
                    res += 1
                    break
                r += 1
            else:
                return -1
    return res


def makeArrayIncreasing_simple(arr1: List[int], arr2: List[int]) -> int:
    arr2 = list(set(arr2))
    r = 0
    res = 0
    for l in range(len(arr1)):
        if (l < len(arr1) - 1 and arr1[l] >= arr1[l + 1]) or (l > 0 and arr1[l] <= arr1[l - 1]):
            while r < len(arr2):
                if arr2[r] > arr1[l - 1]:
                    arr1[l] = arr2[r]
                    res += 1
                    break
                r += 1
            else:
                return -1
    return res


if __name__ == '__main__':
    arr1 = [1, 5, 3, 6, 7]
    arr2 = [1, 3, 2, 4]
    assert 1 == makeArrayIncreasing(arr1, arr2), 'test 1'

    arr1 = [1, 5, 3, 6, 7]
    arr2 = [4, 3, 1]
    assert 2 == makeArrayIncreasing(arr1, arr2), 'test 2'

    arr1 = [1, 5, 3, 6, 7]
    arr2 = [1, 6, 3, 3]
    assert -1 == makeArrayIncreasing(arr1, arr2), 'test 3'

    arr1 = [5, 16, 19, 2, 1, 12, 7, 14, 5, 16]
    arr2 = [6, 17, 4, 3, 6, 13, 4, 3, 18, 17, 16, 7, 14, 1, 16]
    print(makeArrayIncreasing(arr1, arr2))
    assert 8 == makeArrayIncreasing(arr1, arr2), 'test 4'
