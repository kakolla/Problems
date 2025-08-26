from typing import List
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for w in strs:
            s = "".join(sorted(list(w)))
            m[s] = m.get(s, [])
            m[s].append(w)
        


        ans = []
        for _,v in m.items():
            ans.append(v)
        return ans