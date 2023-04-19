from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        res = [self.val]
        nxt = self.next
        while nxt:
            res.append(nxt.val)
            nxt = nxt.next
        return f'{res}'


def addTwoNumbers(
        l1: Optional[ListNode],
        l2: Optional[ListNode]) -> Optional[ListNode]:
    def dfs(root):
        if not root:
            return ''
        return str(root.val) + dfs(root.next)

    num = int(dfs(l1)[::-1]) + int(dfs(l2)[::-1])
    res = ListNode()

    def dfs_r(num: str, cur) -> Optional[ListNode]:
        if not num:
            return None
        cur.next = ListNode(int(num.pop()))
        cur = cur.next
        return dfs_r(num, cur)

    dfs_r(list(str(num)), res)
    return res.next


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    res = ListNode(7, ListNode(0, ListNode(8)))
    assert res.__str__() == addTwoNumbers(l1, l2).__str__()

    l1 = ListNode(0)
    l2 = ListNode(0)
    res = ListNode(0)
    assert res.__str__() == addTwoNumbers(l1, l2).__str__()
