// dam bruh i solved it without any help

class Solution {
    public:
        int minCostClimbingStairs(vector<int>& cost) {
            vector<int> dp(cost.size(), 0);
            
            int n = cost.size(); // num of stairs
            

            dp[n-1] = 1;
            dp[0] = cost[0];
            dp[1] = cost[1];

            // C(n) = min{d(n-1) + C(n), d(n-2) + C(n)}
            for (int i = 2; i < cost.size(); ++i) {
                    dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i]);
            }
            return min(dp[cost.size() - 2], dp[cost.size() -1]);
            



        }
    };
    