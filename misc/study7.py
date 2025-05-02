from typing import List

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # input; given number of slots for each parking space type
        # big = [0, 0, 0, 0]
        big_spaces = [0 for x in range(big)]
        medium_spaces = [0 for x in range(medium)]
        small_spaces = [0 for x in range(small)]
        self.spaces = [-1, big_spaces, medium_spaces, small_spaces]

        

    def addCar(self, carType: int) -> bool:
        parking_space = self.spaces[carType]
        if 0 in parking_space:
            parking_space[parking_space.index(0)] = 1
        else:
            return False
        return True


        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)