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


def reorderList(head: Optional[ListNode]) -> None:
    pass

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    res = ListNode(1, ListNode(4, ListNode(2, ListNode(3))))
    print(reorderList(head))
    # assert res == reorderList(head)