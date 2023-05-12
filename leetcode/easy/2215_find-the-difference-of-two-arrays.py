from typing import List


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    d_1_2 = []
    d_2_1 = []
    for i in nums1:
        if i not in nums2 and i not in d_1_2:
            d_1_2.append(i)
    for j in nums2:
        if j not in nums1 and j not in d_2_1:
            d_2_1.append(j)

    return [d_1_2, d_2_1]


def findDifference_naive(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    assert [[1, 3], [4, 6]] == findDifference(nums1, nums2), 'test 1'

    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    assert [[3], []] == findDifference(nums1, nums2), 'test 2'
