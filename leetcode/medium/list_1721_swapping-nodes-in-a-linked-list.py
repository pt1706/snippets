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


def swapNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    cur = r = l = head

    while cur:
        k -= 1
        if k == 0:
            l = cur
        if k < 0:
            r = r.next
        cur = cur.next
    l.val, r.val = r.val, l.val

    return head


def swapNodes_my(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    res = ListNode(0, head)
    prev = f_p = res
    cur = s_p = f = head

    while cur:
        k -= 1
        if not cur.next:
            s = prev.next
            s_p = prev
        if k <= 0:
            prev = prev.next
        if k == 1:
            f = cur.next
            f_p = cur
        cur = cur.next
    f_p.next = s
    s_p.next = f
    tmp = s.next
    s.next = f.next
    f.next = tmp
    return res.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
    assert res.__repr__() == swapNodes(head, 2).__repr__(), 'test 1'

    head = ListNode(7, ListNode(9, ListNode(6, ListNode(6, ListNode(7, ListNode(8, ListNode(3, ListNode(0, ListNode(9, ListNode(5))))))))))
    res = ListNode(7, ListNode(9, ListNode(6, ListNode(6, ListNode(8, ListNode(7, ListNode(3, ListNode(0, ListNode(9, ListNode(5))))))))))
    assert res.__repr__() == swapNodes(head, 5).__repr__(), 'test 2'

    head = ListNode(1, ListNode(2))
    res = ListNode(2, ListNode(1))
    assert res.__repr__() == swapNodes(head, 1).__repr__(), 'test 3'
