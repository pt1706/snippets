class MyQueue:
    def __init__(self):
        self.data = []
        self.stack = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        while self.data:
            self.stack.append(self.data.pop())
        item = self.stack.pop()
        while self.stack:
            self.data.append(self.stack.pop())
        return item

    def peek(self) -> int:
        while self.data:
            self.stack.append(self.data.pop())
        item = self.stack.pop()
        self.data.append(item)
        while self.stack:
            self.data.append(self.stack.pop())
        return item

    def empty(self) -> bool:
        return len(self.data) == 0


if __name__ == '__main__':
    t = MyQueue()
    t.push(1)
    t.push(2)
    assert 1 == t.peek()
    assert 1 == t.pop()
    assert False is t.empty()