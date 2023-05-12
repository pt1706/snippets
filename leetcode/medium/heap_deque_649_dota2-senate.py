from collections import Counter, deque


def predictPartyVictory(senate: str) -> str:
    offset = len(senate)
    d = deque()
    r = deque()
    for i in range(len(senate)):
        if senate[i] == 'D':
            d.append(i)
        else:
            r.append(i)
    while d and r:
        i_d = d.popleft()
        i_r = r.popleft()
        if i_d < i_r:
            d.append(i_d + offset)
        else:
            r.append(i_r + offset)

    return 'Radiant' if r else 'Dire'


def predictPartyVictory_my_dont_work(senate: str) -> str:
    i = 0
    while len(senate) > 1:
        if i >= len(senate):
            i = 0
        item = senate[i]
        for j in range(len(senate)):
            if item != senate[j]:
                senate = senate[:j] + senate[j + 1:]
                if j > i:
                    i -= 1
                break
        else:
            break
        i += 1
    return 'Radiant' if senate[0] == 'R' else 'Dire'


def predictPartyVictory_naive(senate: str) -> str:
    s = Counter(senate)
    return 'Radiant' if s['R'] > s['D'] else 'Dire' if s['R'] < s['D'] else 'Radiant' if senate[0] == 'R' else 'Dire'


if __name__ == '__main__':
    senate = 'RD'
    assert 'Radiant' == predictPartyVictory(senate), 'test 1'

    senate = 'RDD'
    assert 'Dire' == predictPartyVictory(senate), 'test 2'

    senate = 'DDRRR'
    assert 'Dire' == predictPartyVictory(senate), 'test 3'

    senate = 'DRRD'
    assert 'Dire' == predictPartyVictory(senate), 'test 4'
