class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                print(max_reach)
                print(i)
                return False
            
            # upd max reach
            # if max_reach >= len(nums) - 1: return True # end
            max_reach = max(max_reach, i+nums[i])
            
        return True