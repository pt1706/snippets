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


def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    res = ListNode(0, head)
    cur = head
    m = res
    c = 1
    while cur.next:
        if c:
            m = m.next
            c = 0
        else:
            c += 1
        cur = cur.next

    tmp = m.next
    m.next = tmp.next
    return res.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    res = ListNode(1, ListNode(2, ListNode(4)))
    assert res.__repr__() == deleteMiddle(head).__repr__(), 'test 1'

    head = ListNode(1)
    res = None
    assert res.__repr__() == deleteMiddle(head).__repr__(), 'test 2'

    head = ListNode(2, ListNode(1))
    res = ListNode(2)
    assert res.__repr__() == deleteMiddle(head).__repr__(), 'test 3'

    head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
    res = ListNode(1, ListNode(3, ListNode(4, ListNode(1, ListNode(2, ListNode(6))))))
    assert res.__repr__() == deleteMiddle(head).__repr__(), 'test 3'