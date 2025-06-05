from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return
        first_zero = nums.index(0)
        l = first_zero

        r = l+1
        while r < len(nums):
            if nums[r] != 0:
                # non zero
                # swap 0 with the non zero
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r = l+1
                print("L:" + str(l))
                print("r:" + str(r))
            else:
                # we see a 0, keep going
                r += 1
        
        for k in range(l+1, len(nums)):
            nums[k] = 0
        

        