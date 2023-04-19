from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __repr__(self):
        return f'{self.val}'


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(head, prev):
        if head is None:
            return prev
        else:
            nxt = head.next
            head.next = prev
            return reverse(nxt, head)

    return reverse(head, None)


def reverseList_iter(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    prev = None
    mem = 0
    while cur:
        mem = cur.next
        cur.next = prev
        prev = cur
        cur = mem
    return prev


if __name__ == '__main__':
    head = ListNode(1, ListNode(2))
    res = ListNode(2, ListNode(1))
    assert res == reverseList(head), '1 test'

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    res = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
    assert res == reverseList(head), '2 test'