from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_curr = 0
        max_total = nums[0]
        for i in nums:
            max_curr += i
            max_total = max(max_curr, max_total)
            if max_curr < 0:
                max_curr = 0
            

        return max_total