/*
logic:
cache results from recursion exploring only strictly increasing paths
return maximum you see
*/
#include <vector>

// must be in O(mn)
using namespace std;
class Solution {
    public:
        vector<vector<int>> grid;
        vector<vector<int>> dp;
        int m;
        int n;
        int max_path = 0;

        int recurse(int i, int j) {
            if (dp[i][j] != -1) return dp[i][j]; // already solved

            // do call if it causes strictly increasing
            
            // check if in bounds
            int up = i-1 >=0 ? grid[i-1][j] : -1 ;
            int down = i+1 < m ? grid[i+1][j] : -1;
            int left = j-1 >= 0 ? grid[i][j-1] : -1;
            int right = j+1 < n ? grid[i][j+1] : -1;

            // get best paths from surrounding cells
            int curr = grid[i][j];
            int u = 0, d = 0, l = 0, r = 0;
            if (up > curr) u = recurse(i-1, j);
            if (down > curr) d =  recurse(i+1, j);
            if (left > curr) l = recurse(i, j-1);
            if (right > curr) r = recurse(i, j+1);

            // get max (recurrence relation)
            int max1 = max(u, d);
            int max2 = max(l, r);
            int best = max(max1, max2);

            dp[i][j] = 1 + best; // best is the current cell (1) + best from surrounding paths
            return dp[i][j];
        }


        int longestIncreasingPath(vector<vector<int>>& matrix) {
            // setup
            grid = matrix;
            m = matrix.size();
            n = matrix[0].size();
            dp = vector<vector<int>>(m, vector<int>(n, -1));
            // d(i,j) = max(d(i-1,j), d(i, j-1), d(i+1, j), d(i,j+1))
            for (int i = 0; i < m; ++i) {
                for (int j = 0;j < n; ++j) {
                    max_path = max(max_path, recurse(i, j));
                }

            }
            return max_path;
          
           

        }
    };
    