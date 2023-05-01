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


def isPalindrome(head: Optional[ListNode]):
    def dfs(head, res):
        if not head:
            return res
        res.append(head.val)
        return dfs(head.next, res)
    res = dfs(head, [])
    return res == res[::-1]


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    assert True is isPalindrome(head), '1 test'

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(1))))
    assert False is isPalindrome(head), '2 test'