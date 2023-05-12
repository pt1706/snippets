from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = [self.val]
        item = self.next
        while item:
            res.append(item.val)
            item = item.next
        return str(res)


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    res = ListNode(0, head)
    cur = rem = head
    prev = res
    while cur:
        cur = cur.next
        if n <= 0:
            rem = rem.next
            prev = prev.next
        n -= 1
    prev.next = rem.next
    return res.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
    assert res.__repr__() == removeNthFromEnd(head, 2).__repr__(), 'test 1'

    head = ListNode(1)
    res = head.next
    assert res.__repr__() ==  removeNthFromEnd(head, 1).__repr__(), 'test 2'