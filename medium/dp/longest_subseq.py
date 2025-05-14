class Solution:

    def rec(self, i, j) -> int:
        # i = index in text1
        # j = index in text2
        if i == len(self.text1) or j == len(self.text2):
            return 0
        
        max_len = 0
        if self.text1[i] == self.text2[j]:
            if self.dp[i][j] != -1:
                max_len = self.dp[i][j]
            else:
                max_len = 1 + self.rec(i+1, j+1) # calculate
                self.dp[i][j] = max_len # store
        else:
            # the chars r not equal text1[i] and text2[j]
            if self.dp[i][j] != -1:
                max_len = self.dp[i][j]
            else:
                # try increase window on both (multiple calls)
                max_len = max(self.rec(i+1, j), self.rec(i, j+1))
                self.dp[i][j] = max_len

        return self.dp[i][j]


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.text1 = text1
        self.text2 = text2
        m = len(text1)
        n = len(text2)
        dp = [[-1 for x in range(n)] for y in range(m)]
        self.dp = dp

        return self.rec(0, 0)


              
        