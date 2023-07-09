from typing import List


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    v = [0]

    def dfs(i):
        for j in rooms[i]:
            if j not in v:
                v.append(j)
                if len(v) == len(rooms):
                    break
                if dfs(j):
                    break
        else:
            return False
        return True

    return dfs(0)


if __name__ == '__main__':
    rooms = [[1], [2], [3], []]
    assert True is canVisitAllRooms(rooms), 'test 1'
