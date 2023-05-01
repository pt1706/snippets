from typing import List


def plusOne(digits: List[int]) -> List[int]:
    digits = digits[:]
    if not len(digits):
        return [1]
    if digits[-1] != 9:
        digits[-1] += 1
        return digits
    else:
        digits.pop()
        return plusOne(digits) + [0]


if __name__ == '__main__':
    digits = []
    assert [1] == plusOne(digits)

    digits = [1, 2, 3]
    assert [1, 2, 4] == plusOne(digits)

    digits = [4, 3, 2, 1]
    assert [4, 3, 2, 2] == plusOne(digits)

    digits = [0]
    assert [1] == plusOne(digits)

    digits = [9]
    assert [1, 0] == plusOne(digits)

    digits = [9, 9]
    assert [1, 0, 0] == plusOne(digits)
