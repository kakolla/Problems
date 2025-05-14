# BC: word2 or word1 empty, num of ops is len(other word)
# BC: if both strings "", return 0, thus dimensions are n+1 * m+1 (empty strings after)



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0 for x in range(m+1)] for y in range(n+1)]
        


        # populate dp arr (bottom row)
        for j in range(m+1):
            dp[n][j] = len(word2) - j
        
        # dp arr (right col)
        for i in range(n+1):
            dp[i][m] = len(word1) - i
        
        # bottom up dp
        # i is index of word 1
        # j is index of word 2
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1] # move to next pos for both
                else:
                    # 1 operation must be done (not equal)
                    # delete operation: move word1 forward -> (i+1, j)
                        
                    # insert operation: move word2 forward, need to check
                    # for matching for word 1 -> (i, j+1)
                    
                    # replac operation: same as == but have to add 1 ->(i+1, j+1)

                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

        
        return dp[0][0]
                    



        