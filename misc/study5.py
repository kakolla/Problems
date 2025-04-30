from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if nums[0] == 0 and len(nums) ==1:
            return 0
        # input: arr of nums 
        # output: int, min # of ops to make ALL elements 0 

        times = 0
        nums_no_zero = [x for x in nums if x != 0]
        while (sum(nums_no_zero) != 0):
            nums_no_zero = [x for x in nums_no_zero if x != 0]
            smallest = min(nums_no_zero)
            for i in range (len(nums_no_zero)):
                nums_no_zero[i] -= smallest
                if (nums_no_zero[i] < 0):
                    nums_no_zero[i] = 0
            times += 1
        return times

    def minimumOperationsUsingSet(self, nums: List[int]) -> int:
        numsSet = set(x for x in nums if x != 0)
        # 3  5 19 4
        return len(numsSet) 
    
            


        