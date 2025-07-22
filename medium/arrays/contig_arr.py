from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        mp = {}
        prefix = [0 for i in range(len(nums))]
        # calc prefix sum
        # if 0, subtract 1
        prefix[0] = -1 if nums[0] == 0 else 1
        for i in range(1, len(nums)):
            prev = prefix[i-1]
            if nums[i] == 0:
                prefix[i] = prev + -1
            elif nums[i] == 1:
                prefix[i] = prev + 1
                
        
        # contiguous balanced arr should have prefix sum repeated
        print(prefix)

        # construct hashtable with positions for prefix sums
        for i in range(len(prefix)):
            mp[prefix[i]] = mp.get(prefix[i],[])
            mp[prefix[i]].append(i) # add position
        
        print(mp)
        l = 0
        for k,v in mp.items():
            smallest_pos = v[0]
            largest_pos = v[-1]
            l = max(l, largest_pos - smallest_pos)
            # distance between repeated prefix sums
        
        # edge case: prefix sum 0 is seen, which means 
        # balanced 1s and 0s up to that point        
        # i.e -1 0
        if mp.get(0,-1) != -1:
            l = max(l, mp[0][-1]+1)
            

        return l
    
        # -1 0
        # if there's a 0 -> len between 0s or last 0
        # non zero -> distance between nums