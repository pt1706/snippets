from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    cur = n + m - 1
    while n > 0 and m > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[cur] = nums1[m - 1]
            m -= 1
        else:
            nums1[cur] = nums2[n - 1]
            n -= 1
        cur -= 1

    while n > 0:
        nums1[cur] = nums2[n - 1]
        n -= 1
        cur -= 1


if __name__ == '__main__':
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    assert [1, 2] == nums1

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    assert [1, 2, 2, 3, 5, 6] == nums1

    nums1 = [1, 2, 3, 4, 0, 0]
    m = 4
    nums2 = [2, 6]
    n = 2
    merge(nums1, m, nums2, n)
    assert [1, 2, 2, 3, 4, 6] == nums1

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    assert [1] == nums1

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    assert [1] == nums1