class UndergroundSystem:
    def __init__(self):
        self.start = {}
        self.avgtime = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time = t - self.start[id][1]
        stations = (self.start[id][0], stationName)
        if stations not in self.avgtime:
            self.avgtime[stations] = [time, 1]
        else:
            self.avgtime[stations][0] += time
            self.avgtime[stations][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        stations = (startStation, endStation)
        time = self.avgtime[stations][0]
        count = self.avgtime[stations][1]
        return time / count


if __name__ == '__main__':
    u = UndergroundSystem()
    u.checkIn(45, 'Leyton', 3)
    u.checkIn(32, 'Paradise', 8)
    u.checkIn(27, 'Leyton', 10)
    u.checkOut(45, 'Waterloo', 15)
    u.checkOut(27, 'Waterloo', 20)
    u.checkOut(32, 'Cambridge', 22)
    assert 14.0 == u.getAverageTime('Paradise', 'Cambridge'), 'time 1'
    assert 11.0 == u.getAverageTime('Leyton', 'Waterloo'), 'time 2'
    u.checkIn(10, 'Leyton', 24)
    assert 11.0 == u.getAverageTime('Leyton', 'Waterloo'), 'time 3'
    u.checkOut(10, 'Waterloo', 38)
    assert 12.0 == u.getAverageTime('Leyton', 'Waterloo'), 'time 4'
