









class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        # check if start of a consec subseq
        # if yes, count it
        # if not, keep going
        
        s = set()
        for x in nums:
            s.add(x)

        longest = 1
        for num in s:
            if num-1 not in s:
                curr = num
                c = 1
                # start
                while curr +1 in s:
                    curr += 1
                    c +=1
                longest = max(longest, c)

                    
        return longest

                


                    
