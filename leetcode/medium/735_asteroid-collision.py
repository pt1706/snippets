from collections import deque
from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []
    asteroids = deque(asteroids)
    while asteroids:
        nxt = asteroids.popleft()
        while stack and (nxt < 0 and stack[-1] > 0):
            lst = stack.pop()
            if abs(nxt) == abs(lst):
                nxt = None
                break
            elif abs(nxt) > abs(lst):
                continue
            else:
                nxt = lst
        if nxt:
            stack.append(nxt)

    return stack


if __name__ == '__main__':
    asteroids = [5, 10, -5]
    assert [5, 10] == asteroidCollision(asteroids), 'test 1'

    asteroids = [8, -8]
    assert [] == asteroidCollision(asteroids), 'test 2'

    asteroids = [10, 2, -5]
    assert [10] == asteroidCollision(asteroids), 'test 3'

    asteroids = [-2, -1, 1, 2]
    assert [-2, -1, 1, 2] == asteroidCollision(asteroids), 'test 4'