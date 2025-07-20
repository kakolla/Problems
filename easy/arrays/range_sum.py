from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        psums = [0 for i in range(len(nums))]
        # calculate prefix sum
        for i in range(len(nums)):
            if i == 0:
                psums[i] = nums[i]
            else:
                psums[i] = psums[i-1] + nums[i]
        self.psums = psums
        

    def sumRange(self, left: int, right: int) -> int:
        # O(1)
        if left == 0:
            return self.psums[right] # inclusive 
        return self.psums[right] - self.psums[left-1]

"""
1 1 1 
0,2
psum = 1 2 3
3

"""