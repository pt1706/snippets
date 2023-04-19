from collections import deque


class MyStack:
    def __init__(self):
        self.data = deque()

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        for i in range(len(self.data) - 1):
            item = self.data.popleft()
            self.data.append(item)
        return self.data.popleft()

    def top(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        return len(self.data) == 0


if __name__ == '__main__':
    t = MyStack()
    t.empty()