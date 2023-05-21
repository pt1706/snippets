from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    r, l = 0, len(numbers) - 1
    while r != l:
        if numbers[r] + numbers[l] == target:
            return [r + 1, l + 1]
        if numbers[r] + numbers[l] > target:
            l -= 1
        else:
            r += 1
    return [0, 0]


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    assert [1, 2] == twoSum(numbers, target), 'test 1'

    numbers = [2, 3, 4]
    target = 6
    assert [1, 3] == twoSum(numbers, target), 'test 2'