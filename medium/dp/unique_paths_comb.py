import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m-1 + n-1 choose 2
        # 2 directions
        return math.factorial(m-1+n-1) // (2*math.factorial(m+n-4))