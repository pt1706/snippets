from typing import List


def average(salary: List[int]) -> float:
    min_w = min(salary[0], salary[1])
    max_w = max(salary[0], salary[1])
    res = 0
    for i in salary[2:]:
        if i < min_w:
            res += min_w
            min_w = i
        elif i > max_w:
            res += max_w
            max_w = i
        else:
            res += i
    return res / (len(salary) - 2)


if __name__ == '__main__':
    salary = [1000, 2000, 3000]
    assert 2000 == average(salary), 'test 1'

    salary = [4000, 3000, 1000, 2000]
    assert 2500 == average(salary), 'test 2'