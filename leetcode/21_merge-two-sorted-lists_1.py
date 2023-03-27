from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = f'{self.val}'
        if self.next:
            tail = self.next
            while tail:
                res += f', {tail.val}'
                tail = tail.next
        return res


class Solution:
    def mergeTwoLists(
            self,
            list1: Optional[ListNode],
            list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        res = ListNode()
        tail = res
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return res.next


list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

if __name__ == '__main__':
    assert '1, 1, 2, 3, 3, 4' == Solution().mergeTwoLists(list1, list2).__str__()