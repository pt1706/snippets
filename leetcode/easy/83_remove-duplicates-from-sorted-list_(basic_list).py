from typing import List


def deleteDuplicates(head: List[int]) -> List[int]:
    l = 0
    for r in range(1, len(head)):
        if head[l] != head[r]:
            l += 1
            head[l] = head[r]
    return head[:l + 1]


if __name__ == '__main__':
    assert [1, 2] == deleteDuplicates([1, 1, 2])
    assert [1, 2, 3] == deleteDuplicates([1, 1, 2, 3, 3])
    assert [1, 2, 3, 4, 6, 8, 9] == deleteDuplicates([1, 1, 2, 3, 3, 4, 4, 6, 8, 8, 9])

