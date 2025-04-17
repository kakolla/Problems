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
            
            // check if in bounds
            // run call if it causes strictly increasing

            int curr = grid[i][j];
            int up = i-1 >=0 ? grid[i-1][j] : -1 ;
            int down = i+1 < m ? grid[i+1][j] : -1;
            int left = j-1 >= 0 ? grid[i][j-1] : -1;
            int right = j+1 < n ? grid[i][j+1] : -1;

            int u, d, l, r;
            if (up > curr) u = recurse(i-1, j);
            if (down > curr) d =  recurse(i+1, j);
            if (left > curr) l = recurse(i, j-1);
            if (right > curr) r = recurse(i, j+1);





        }
        int longestIncreasingPath(vector<vector<int>>& matrix) {
            // setup
            grid = matrix;
            m = matrix.size();
            n = matrix[m].size();
            dp = vector<vector<int>>(m, vector<int>(n, -1));
            // d(i,j) = max(d(i-1,j), d(i, j-1), d(i+1, j), d(i,j+1))

            


            

        }
    };
    