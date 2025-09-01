from typing import List

class Solution:

    def get_ones(self, i: int) -> int:
        
        n = 0
        t = i
        while (t != 0):
            if t % 2 == 1:
                n += 1
            t = t // 2

        return n

    def countBits(self, n: int) -> List[int]:
        ans = [0 for i in range(n+1)]

        for i in range(n+1):
            ans[i] = self.get_ones(i)

        return ans

        