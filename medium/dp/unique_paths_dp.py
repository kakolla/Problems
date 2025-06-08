class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(m)] for j in range(n)]

        # rec rel
        # d(i,j) = d(i-1,j) + d(i,j-1)

        # base cases
        for i in range(n):
            dp[i][0] = 1 # only one way to get here
        
        for j in range(m):
            dp[0][j] = 1 # same

        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
            
        return dp[n-1][m-1]
        