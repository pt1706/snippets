from typing import List


def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort()
    d = arr[0] - arr[1]
    for i in range(2, len(arr)):
        if arr[i - 1] - arr[i] != d:
            return False
    return True


if __name__ == '__main__':
    arr = [3, 5, 1]
    assert True is canMakeArithmeticProgression(arr), 'test 1'

    arr = [1, 2, 4]
    assert False is canMakeArithmeticProgression(arr), 'test 2'