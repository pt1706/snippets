# ------------------BFS with list-----------------------------------

def bfs(graf: dict, start_point: str = 'You', clause: str = 'A') -> str:
    queue = [start_point]
    queue += graf[start_point][:]
    visited = [start_point]
    while queue:
        item = queue.pop(0)
        if item[0] == clause:
            return item
        visited += [item]
        if graf.get(item):
            for child in graf[item]:
                if child not in visited:
                    queue.append(child)
    return "Nothing find"


graf = dict(You=['Bob', 'Clear', 'Alisa'],
            Alisa=['You', 'Pegge'],
            Bob=['Anudg', 'You', 'Pegge'],
            Clear=['Jonny', 'You', 'Tom'])

if __name__ == '__main__':
    assert bfs(graf, 'You', 'A') == 'Alisa'
    assert bfs(graf, 'You', 'P') == 'Pegge'
    assert bfs(graf, 'You', 'T') == 'Tom'
    assert bfs(graf, 'You', 'Y') == 'You'
    print('all test passed')

# ------------------BFS with deque-----------------------------------

from collections import deque # noqa


def bfs(graf: dict, start_point: str = 'You', clause: str = 'A') -> str:
    queue = deque([start_point])
    queue += graf[start_point][:]
    visited = [start_point]
    while queue:
        item = queue.popleft()
        if item[0] == clause:
            return item
        visited += [item]
        if graf.get(item):
            for child in graf[item]:
                if child not in visited:
                    queue.append(child)
    return "Nothing find"


graf = dict(You=['Bob', 'Clear', 'Alisa'],
            Alisa=['You', 'Pegge'],
            Bob=['Anudg', 'You', 'Pegge'],
            Clear=['Jonny', 'You', 'Tom'])

if __name__ == '__main__':
    assert bfs(graf, 'You', 'A') == 'Alisa'
    assert bfs(graf, 'You', 'P') == 'Pegge'
    assert bfs(graf, 'You', 'T') == 'Tom'
    assert bfs(graf, 'You', 'Y') == 'You'
    print('all test passed')
