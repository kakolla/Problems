from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        t = nums[0]
        while (l <= r):
            if l == r:
                return min(t, nums[l])
            m = (l+r)//2
            if (nums[m] < nums[r]):
                r = m-1
                t = min(t, nums[m])
            elif nums[m] > nums[r]:
                l = m+1
                t = min(t, nums[m])
        
        return t

#h
                