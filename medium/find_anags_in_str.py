from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        # return start indices of anagrams of p 

        l = 0
        r = len(p)

        # sort p
        p = "".join(sorted(list(p)))

        while r <= len(s):
            cur = s[l:r]
            cur = "".join(sorted(list(cur))) # sorted version
            if cur == p:
                ans.append(l)
            l += 1
            r +=1
            

        return ans


        