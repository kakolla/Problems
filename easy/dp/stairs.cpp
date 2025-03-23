// Bottom-up approach, also use O(n) memory which can be improved

class Solution {
    public:
        int climbStairs(int n) {
    
            vector<int> dp(n+1, 0); // allocate n+1 vals (0, ... n)
    
            // base cases
            dp[n] = 1; // on the last step, there is 1 way to get to the last step (stay)
            dp[n-1] = 1; // on 2nd last step, one way to get to the last step (jump 1)
    
            // on a subproblem, it depends on the next 2 solns in array (1 steps, or 2 steps)
            for (int i = n-2; i >= 0; --i) {
                dp[i] = dp[i+2] + dp[i+1];
            }
    
            // see array
            for (auto e : dp ) {
                cout << e << endl;
            }
    
    
            return dp[0]; // return the top subproblem 
    
        }
    };
    