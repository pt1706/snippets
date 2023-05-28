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


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    d = ListNode(0, head)
    o = head
    e = head.next
    d_e = e

    while e and o:
        o.next = e.next
        if not o.next:
            break
        o = o.next
        if not o.next:
            e.next = None
            break
        e.next = o.next
        e = e.next
    o.next = d_e

    return d.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = ListNode(1, ListNode(3, ListNode(5, ListNode(2, ListNode(4)))))
    assert res.__repr__() == oddEvenList(head).__repr__(), 'test 1'

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
    res = ListNode(1, ListNode(3, ListNode(5, ListNode(7, ListNode(2, ListNode(4, ListNode(6, ListNode(8))))))))
    assert res.__repr__() == oddEvenList(head).__repr__(), 'test 3'
