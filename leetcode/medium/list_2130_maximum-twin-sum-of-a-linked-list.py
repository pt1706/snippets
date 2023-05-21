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


def pairSum(head: Optional[ListNode]) -> int:
    s, f = head, head
    c = 1
    while f:
        f = f.next
        if c == 1:
            s = s.next
            c -= 1
        else:
            c += 1
    prev = s
    cur = s.next
    prev.next = None
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    res = 0
    while prev:
        res = max(res, head.val + prev.val)
        head = head.next
        prev = prev.next

    return res




def pairSum_simple(head: Optional[ListNode]) -> int:
    """it works"""
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next

    res = 0
    l, r = 0, len(vals) - 1
    while l < r:
        res = max(res, vals[l] + vals[r])
        l += 1
        r -= 1
    return res


if __name__ == '__main__':
    head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
    assert 6 == pairSum(head), 'test 1'

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(8))))))
    assert 9 == pairSum(head), 'test 2'
