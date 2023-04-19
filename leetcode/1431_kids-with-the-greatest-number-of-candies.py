from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    max_q = max(candies)
    return [x + extraCandies >= max_q for x in candies]


if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    output = [True, True, True, False, True]
    assert output == kidsWithCandies(candies, extraCandies)