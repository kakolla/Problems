
from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # input: list of boxes: numOfBoxes, numofUnitsPerBox
        # also truck size
        
        # output: max units on the truck


        # make sure we want to not exceed the num of Boxes** on the truck
        boxTypes.sort(key= lambda x : x[1], reverse=True) # sort based on 2nd value
        
        # greedy: take as much as u can until truck full
        max_units = 0
        boxes = 0
        for x in boxTypes:
            for k in range(x[0]):
                if (boxes + 1 <= truckSize):
                    max_units += 1 * x[1]
                    boxes += 1


        return max_units


       
