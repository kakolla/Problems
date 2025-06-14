from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f = {}
        for l in arr:
            f[l] = f.get(l, 0) + 1

        # multi set kinda
        return sorted(set(f.values())) == sorted(f.values())
            
        
        