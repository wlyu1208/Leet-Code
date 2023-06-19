class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.array = [big, medium, small]
        

    def addCar(self, carType: int) -> bool:
        if self.array[carType-1] > 0:
            self.array[carType-1] -= 1
            return True
        else:
            return False
