from typing import List


def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    stack = []
    for item in pushed:
        stack.append(item)
        while stack and stack[-1] == popped[0]:
            popped.pop(0)
            stack.pop()
    return len(stack) == 0


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    assert False is validateStackSequences(pushed, popped), 'test 1'

    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    assert True is validateStackSequences(pushed, popped), 'test 2'