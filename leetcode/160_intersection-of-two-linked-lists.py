from typing import List, Optional


class ListNode:
    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """
    Find length of both arrow
    Then move left or right cursor until number of rest node become equal
    Move cursors together until find same number
    """
    curA = headA
    curB = headB
    len_A, len_B = 0, 0
    while curA or curB:
        len_A = len_A + 1 if curA else len_A
        len_B = len_B + 1 if curB else len_B
        curA = curA.next if curA else curA
        curB = curB.next if curB else curB

    curA = headA
    curB = headB
    while abs(len_A - len_B) != 0:
        curA = curA.next if len_A - len_B > 0 else curA
        curB = curB.next if len_B - len_A > 0 else curB
        len_A = len_A + 1 if len_B - len_A > 0 else len_A
        len_B = len_B + 1 if len_A - len_B > 0 else len_B

    while curB:
        if curB == curA:
            return curA
        curA = curA.next
        curB = curB.next
    return None


def getIntersectionNode_extra_mem(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    curA = headA
    curB = headB
    visited = set()
    while curA:
        visited.add(curA)
        curA = curA.next

    while curB:
        if curB in visited:
            return curB
        curB = curB.next
    else:
        return None


def getIntersectionNode_slow(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    curA = headA
    curB = headB
    counter = 0
    while curA:
        while curB:
            counter += 1
            if curA == curB:
                return curA
            curB = curB.next
        curB = headB
        curA = curA.next
    else:
        return None


if __name__ == '__main__':
    common = ListNode(8, ListNode(4, ListNode(5)))
    headA = ListNode(4, ListNode(1, common))
    headB = ListNode(5, ListNode(6, ListNode(1, common)))
    assert common == getIntersectionNode(headA, headB), '1 test'

    common = ListNode(2, ListNode(4))
    headA = ListNode(1, ListNode(9, ListNode(1, common)))
    headB = ListNode(3, common)
    assert common == getIntersectionNode(headA, headB), '2 test'

    common = None
    headA = ListNode(2, ListNode(6, ListNode(4)))
    headB = ListNode(2, ListNode(5))
    assert common == getIntersectionNode(headA, headB), '3 test'
