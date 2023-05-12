import heapq
from collections import deque
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
    if n == 0:
        return len(tasks)
    h = {}
    for k in tasks:
        h[k] = h.setdefault(k, 0) - 1
    h = list(h.values())
    heapq.heapify(h)
    q = deque()
    t = 0
    while h or q:
        t += 1
        if h:
            item = heapq.heappop(h) + 1
            if item:
                q.append((item, t + n))

        if q and q[0][1] == t:
            heapq.heappush(h, q.popleft()[0])
    return t


def leastInterval_doesn_work(tasks: List[str], n: int) -> int:
    if n == 0:
        return len(tasks)
    d = {k: 0 for k in tasks}
    time = 0
    tasks.sort()
    while tasks:
        time += 1
        for i in range(len(tasks)):
            item = tasks[i]
            if d[item] == 0 or time >= d[item] + 1 + n:
                d[item] = time
                tasks = tasks[:i] + tasks[i + 1:]
                tasks.sort()
                break
    return time


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    assert 8 == leastInterval(tasks, n), 'test 1'

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 0
    assert 6 == leastInterval(tasks, n), 'test 2'

    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    assert 16 == leastInterval(tasks, n), 'test 3'

    tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"]
    n = 2
    assert 12 == leastInterval(tasks, n), 'test 4'
