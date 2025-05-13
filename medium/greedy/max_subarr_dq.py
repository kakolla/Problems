from typing import List

class Solution:
    def recurse(self, nums, l, r) -> int:
        if l == r:
            return nums[l]
        
        m = (l+r)//2

        max_left = self.recurse(nums, l, m)
        max_right = self.recurse(nums, m+1, r)

        # spanning across middle
        best_left = float('-inf')
        temp = 0
        for k in range(m, l-1, -1):
            temp += nums[k]
            best_left = max(best_left, temp)

        best_right = float('-inf')
        temp = 0
        for k in range(m+1, r+1):
            temp += nums[k]
            best_right = max(best_right, temp)
        
        middle_max = best_left + best_right
    
        return max(max(max_left, max_right), middle_max)
        
            




    def maxSubArray(self, nums: List[int]) -> int:
        return self.recurse(nums, 0, len(nums) - 1)
        
        
        


