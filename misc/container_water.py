




from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        l, r = 0 , n-1


        maxarea = 0
        for i in range(n):
            # move the smaller ptr
            area = min(height[l], height[r]) * abs(l-r)
            maxarea = max(maxarea ,area)
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1

        return maxarea


        


        

