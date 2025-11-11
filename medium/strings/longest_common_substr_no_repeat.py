"""
sliding window
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        seen = set()
        l,r = 0, 0
        max_len = 0

        while r < len(s):
            while s[r] in seen:
                # shrink window from left
                seen.remove(s[l])
                l +=1 
            
            # grow window if we don't have repeating chars
            max_len = max(max_len, r-l+1)
            seen.add(s[r])
            r += 1
        
        return max_len