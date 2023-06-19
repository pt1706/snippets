from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0 for _ in range(len(temperatures))]
    stack = []
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][1]:
            inx, temp = stack.pop()
            res[inx] = i - inx
        stack.append(([i, t]))
    return res


def dailyTemperatures_simple(temperatures: List[int]) -> List[int]:
    res = [0 for _ in range(len(temperatures))]
    for i in range(len(temperatures) - 1):
        j = i + 1
        while j < len(temperatures) and temperatures[i] >= temperatures[j]:
            j += 1
        if j >= len(temperatures):
            continue
        else:
            res[i] = j - i
    return res


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    res = [1, 1, 4, 2, 1, 1, 0, 0]
    assert res == dailyTemperatures(temperatures), 'test 1'

    temperatures = [30, 40, 50, 60]
    res = [1, 1, 1, 0]
    assert res == dailyTemperatures(temperatures), 'test 2'

    temperatures = [30, 60, 90]
    res = [1, 1, 0]
    assert res == dailyTemperatures(temperatures), 'test 3'
