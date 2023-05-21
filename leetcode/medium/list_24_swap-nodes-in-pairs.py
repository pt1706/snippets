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


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    res = ListNode(0, head)
    c_1 = head
    c_2 = head.next
    prev = res
    while c_1 and c_2:
        c_1.next = c_2.next
        prev.next = c_2
        c_2.next = c_1
        if not c_1.next:
            break
        prev = c_1
        c_1 = c_1.next
        if not c_1.next:
            break
        c_2 = c_1.next

    return res.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    res = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))
    assert res.__repr__() == swapPairs(head).__repr__(), 'test 1'
