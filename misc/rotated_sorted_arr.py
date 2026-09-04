



from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 4,5,6,7,0,1,2
        
        # look at the bounds
        # if m > r, go to the right
        # if m < r, go to the left

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # check if we are at the smallest number
            if nums[m] < nums[m-1]:
                return nums[m]
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        print(nums[l])
        return nums[l]

