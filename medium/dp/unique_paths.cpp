#include <vector>

using namespace std;
class Solution {
    public:
        int uniquePaths(int m, int n) {
            // mxn gridj
            vector<vector<int>> dp(m, vector<int>(n,0));
            
            // base cases
            for (int i = 0; i < n; ++i) {
                dp[0][i] = 1;
            }

            for (int i = 0; i < m; ++i) {
                dp[i][0] = 1;
            }


            // d(i, j) = d(i-1,j) + d(i,j-1)
            for (int i = 0; i < m; ++i ) {
                for (int j = 0; j < n; ++j ) {
                    if (i-1 >= 0 && j-1 >= 0) {
                            dp[i][j] = dp[i-1][j] + dp[i][j-1];

                    }

                }
            }
            return dp[m-1][n-1];

        }
    };
    