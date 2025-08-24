from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # build hash set - can also use map
        s = set()
        for i in range(len(nums)):
            s.add(nums[i])
        
        # count sequences
        max_l = 0
        l = 0
        nums = list(set(nums))
        for i in range(len(nums)):
            if nums[i]-1 not in s:
                # if num less doesnt exist
                # start building sequence
                l = 1
                next = nums[i] +1
                while next in s:
                    l += 1
                    next += 1
                
                max_l = max(max_l, l)
                l = 0


        return max_l