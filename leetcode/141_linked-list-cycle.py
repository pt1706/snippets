from typing import Optional


class ListNode:
    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node


def hasCycle(head: Optional[ListNode]) -> bool:
    visited = []
    cur = head
    while cur:
        if cur.next is None:
            return False
        if cur.next in visited:
            return True
        visited.append(cur)
        cur = cur.next


if __name__ == '__main__':
    head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4,))))
    assert False is hasCycle(head)

    n_2 = ListNode(0)
    n_1 = ListNode(2, n_2)
    head = ListNode(3, n_1)
    n_3 = ListNode(-4, n_1)
    n_2.next = n_3
    assert True is hasCycle(head)