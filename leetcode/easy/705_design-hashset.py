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


class MyHashSet:
    def __init__(self):
        self.array = [[] for _ in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.array)
        row = self.array[index]
        if key not in row:
            row.append(key)

    def remove(self, key: int) -> None:
        index = key % len(self.array)
        row = self.array[index]
        if key in row:
            row.remove(key)
            return key

    def contains(self, key: int) -> bool:
        index = key % len(self.array)
        row = self.array[index]
        if key in row:
            return True
        else:
            return False


class MyHashSet_NC_with_ListNode:
    def __init__(self):
        self.array = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.array)
        cur = self.array[index]
        while cur.next:
            if cur.next.val == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.array)
        cur = self.array[index]
        while cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
                return key
            cur = cur.next
        return None

    def contains(self, key: int) -> bool:
        index = key % len(self.array)
        cur = self.array[index]
        while cur.next:
            if cur.next.val == key:
                return True
            cur = cur.next
        return False


class MyHashSet_my:
    """stupid solution without hash funaction"""
    def __init__(self):
        self.hash = []

    def add(self, key: int) -> None:
        if key not in self.hash:
            self.hash.append(key)

    def remove(self, key: int) -> None:
        if key in self.hash:
            self.hash.remove(key)
            return key

    def contains(self, key: int) -> bool:
        if key in self.hash:
            return True
        else:
            return False


if __name__ == '__main__':
    m = MyHashSet()
    m.add(1)
    m.add(2)
    assert True is m.contains(1)
    assert False is m.contains(3)
    m.add(2)
    assert True is m.contains(2)
    assert 2 == m.remove(2)
    assert False is m.contains(2)