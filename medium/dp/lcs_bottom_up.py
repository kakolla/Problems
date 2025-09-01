class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]


        for i in range(len(text2)-1, -1, -1):
            for j in range (len(text1)-1, -1, -1):

                if text1[j] == text2[i]:
                    # match, 1 character added to the lcs
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    # move one word forward for both, get the max
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    
        return dp[0][0]
    