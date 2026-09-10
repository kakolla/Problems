










class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        lg = 0




        from collections import defaultdict
        freq =  defaultdict(int)
        l, r = 0, 0

        while r < n:
            if freq[s[r]] == 0:
                pass
            else:
                while freq[s[r]] != 0:
                    freq[s[l]] -= 1
                    l += 1
            freq[s[r]] += 1
            lg = max(lg, r - l + 1)
            r += 1
        return lg

            



        

         
        











