// nice solved with minimal help in approach
// same 1d dp method 
// just be careful about the recurrence relation

#include <vector>
class Solution {
    public:
        int rob(vector<int>& nums) {
            if (nums.size() == 1) return nums[0];
            if (nums.size() <= 2) {
                return max(nums[0], nums[1]);
            }


            vector<int> dp(nums.size(), 0);
            
            // rob(i) = max(nums[i] + rob(i-2), rob(i-1))
            dp[0] = nums[0];
            dp[1] = max(nums[0], nums[1]); // consider 1st or 2nd house to start with
            
            int n = nums.size();
            for (int i = 2; i < n; ++i) {
                dp[i] = max(nums[i] + dp[i-2], dp[i-1]);
            }
            return dp[n-1];


        }
    };
    


