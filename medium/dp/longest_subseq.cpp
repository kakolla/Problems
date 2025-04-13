/*
This is top-down approach with recursion + memoization
acc makes sense
start at the top it will spawn a lot of recursive calls
but it will cache it so it improves runtime

thinking:
iterating thru both strings with i, j
if i == j
    return max length = 1 + rec()
else
    return max length = max( rec(i+1, j), rec(i, j+1) )
    // calls will explore extending both windows by one
    // cache them for later
*/

#include <string>
#include <vector>

using namespace std;
class Solution {
    public:
        string text1;
        string text2;       
        vector<vector<int>> dp;
            

        int rec(int i, int j) {
            // i - index in text1
            // j - index  in text2

            // out of bounds
            if (i == text1.size() || j == text2.size()) return 0;


            // choose to extend subsequence ( same chars)
            // or explore both paths by one index at a time
            // keep track of longest subseq seen
            int max_length = 0;
            if (text1[i] == text2[j]) {
                // incr length by 1
                if (dp[i][j] != -1) {
                    max_length = dp[i][j];
                } else {
                    // soln hasn't been calced yet
                    max_length = 1 + rec(i+1, j+1);
                    dp[i][j] = max_length; // store after calc
                }
            } else {
                // with recursion can try increasing window on both
                if (dp[i][j] != -1) {
                    max_length = dp[i][j];
                } else {
                    max_length = max(rec(i+1, j), rec(i, j+1));
                    dp[i][j] = max_length;
                }
            
            }
            return max_length;


        }
        int longestCommonSubsequence(string text1, string text2) {
            this->text1 = text1;
            this->text2 = text2;
            
            int m = text1.size();
            int n = text2.size();
            this->dp = vector<vector<int>>(m, vector<int>(n, -1));
            
            return rec(0, 0);
            
        }
        
    };
    