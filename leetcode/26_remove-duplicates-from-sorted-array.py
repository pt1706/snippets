from typing import List


def removeDuplicates(nums: List[int]):
    k = 0
    item = 10000
    index = -1
    while item >= nums[index]:
        item = nums.pop(index)
        if item in nums:
            k += 1
            nums.append('_')
            index -= 1
        else:
            nums.insert(0, item)
    return k, nums


if __name__ == '__main__':
    print(*removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(*removeDuplicates([1, 1, 2]))