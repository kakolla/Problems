from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [0 for i in range(len(candies))]

        m = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= m:
                result[i] = True
            else:
                result[i] = False

        return result
        
