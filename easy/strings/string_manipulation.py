from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1
        for i in range(len(s)):
            if i == n: # odd case
                break
            if i > n:
                break # even case

            s[i], s[n] = s[n], s[i]
            n -= 1
        
        return

