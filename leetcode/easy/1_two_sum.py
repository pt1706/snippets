import random
from typing import List, Tuple


list(random.choice(range(0, 101)) for x in range(200))
nums = [50, 43, 94, 56, 23, 3, 28, 25, 62, 37, 72, 36, 95, 58, 91, 51, 41, 8, 7, 56, 34, 18, 2, 97, 2, 6, 93, 71, 20, 83, 99, 75, 76, 52, 11, 9, 74, 0, 100, 4, 90, 23, 36, 34, 78, 39, 48, 13, 5, 59, 30, 5, 18, 66, 32, 60, 53, 33, 54, 58, 36, 58, 40, 42, 62, 30, 18, 70, 19, 90, 77, 32, 55, 32, 66, 100, 28, 99, 11, 95, 85, 45, 95, 0, 0, 94, 83, 65, 21, 61, 46, 35, 35, 35, 42, 40, 2, 46, 59, 7, 21, 79, 80, 9, 47, 14, 45, 10, 55, 38, 63, 41, 56, 89, 3, 95, 32, 21, 90, 73, 55, 81, 64, 78, 88, 1, 69, 76, 80, 91, 24, 2, 92, 92, 53, 17, 42, 9, 0, 91, 75, 83, 70, 53, 38, 99, 26, 92, 11, 48, 96, 33, 90, 62, 8, 68, 81, 49, 73, 53, 65, 65, 96, 47, 89, 58, 52, 15, 50, 3, 19, 7, 87, 52, 18, 96, 38, 95, 98, 31, 72, 84, 43, 28, 100, 70, 12, 43, 15, 15, 82, 86, 59, 83, 95, 84, 91, 49, 90, 54]


def twoSum(nums: List[int], target: int) -> Tuple[List[int], int]:
    counter = 0
    for index_1 in (range(len(nums))):
        for index_2 in (range(index_1 + 1, len(nums))):
            counter += 1
            if nums[index_1] + nums[index_2] == target:
                return [index_1, index_2], counter
    return [0, 0], 0


def twoSum_fast(nums: List[int], target: int) -> Tuple[List[int], int]:
    counter = 0
    visited = {}
    for i, value in enumerate(nums):
        counter += 1
        diff = target - value
        if visited.get(diff):
            return [visited[diff], i], counter
        visited[value] = i
    return [0, 0], 0


if __name__ == '__main__':
    print(twoSum(nums, 19))
    print(twoSum_fast(nums, 19))