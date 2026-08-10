














class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        f = {}
        while r < len(nums):
            # [0,0,1,1,1,1,2,3,3]
            while r < len(nums) and f.get(nums[r],0) == 2:
                r += 1
            if r >= len(nums):
                break
            nums[l] = nums[r]
            f[nums[l]] = f.get(nums[l], 0) + 1
            l += 1
            r += 1
            
        return l





        pass

        
