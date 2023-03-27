from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = f'[{self.val}'
        next_val = self.next
        while next_val is not None:
            res += f', {next_val.val}'
            next_val = next_val.next
        return res + ']'


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    if not cur:
        return cur
    while cur.next is not None:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


if __name__ == '__main__':
    lst_test = []
    res = []
    print(res)
    print(deleteDuplicates(lst_test))
    lst_test = ListNode(0, (ListNode(1, ListNode(1, ListNode(2)))))
    res = ListNode(0, (ListNode(1, ListNode(2))))
    print(res)
    print(deleteDuplicates(lst_test))
    # assert res == deleteDuplicates(lst_test)
    lst_test = ListNode(0, (ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))))
    res = ListNode(0, (ListNode(1, ListNode(2, ListNode(3)))))
    print(res)
    print(deleteDuplicates(lst_test))
    # assert res == deleteDuplicates(lst_test)

