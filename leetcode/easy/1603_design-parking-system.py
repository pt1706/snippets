class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if self.small and carType == 3:
            self.small -= 1
            return True
        elif self.medium and carType == 2:
            self.medium -= 1
            return True
        elif self.big and carType == 1:
            self.big -= 1
            return True
        else:
            return False


if __name__ == '__main__':
    p = ParkingSystem(1, 1, 0)
    assert True is p.addCar(1)
    assert True is p.addCar(2)
    assert False is p.addCar(3)
    assert False is p.addCar(1)