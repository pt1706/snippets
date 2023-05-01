from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    res = ListNode(0, head)
    head = res
    cur = head.next
    while cur:
        if cur.val != val:
            head.next = cur
            head = cur
        head.next = cur.next
        cur = cur.next
    return res.next


if __name__ == '__main__':
    head = None
    val = 1
    res = None
    assert res == removeElements(head, val), '1 test'

    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    val = 6
    res = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert res == removeElements(head, val), '2 test'

