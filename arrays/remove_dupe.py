class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seen = []
        for x in range(len(nums)):
            if nums[x] in seen:
                nums[x] = -101
            if nums[x] not in seen:
                seen.append(nums[x])
        
        temp = 0
        for x in range(len(nums)):
            if nums[x] == -101:
                for l in range(x, len(nums)):
                    if nums[l] != -101:
                        nums[x] = nums[l]
                        nums[l] = -101
                        break
        
        s = 0
        for e in nums:
            if e == -101:
                break
            s += 1
        return s