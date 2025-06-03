from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = 0
        for i in range(len(flowerbed)):
            # check if we can place flower
            p = i-1 if i-1 >=0 else 0 # previous plot
            c = i
            t = i+1 if i+1 < len(flowerbed) else i
            if not flowerbed[p] and not flowerbed[c] and not flowerbed[t]:
                flowerbed[c] = 1
                k +=1
            
            if k == n:
                return True
            
        print(k)
        if k == n:
            return True
        elif k < n:
            return False
        else:
            return True
    


        
