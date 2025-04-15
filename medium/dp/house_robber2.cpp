/*
Same as hosue robber 1 
except you exclude robbing the first hosue and run same algo
and then exclude the lsat house
take the max value you saw
*/


class Solution {
    public:

        int robSubset(vector<int>& nums) {
            int n = nums.size();
            if (n==0) return 0;
            if (n==1) return nums[0];
            vector<int> dp(n, 0);
            dp[0] = nums[0];
            dp[1] = max(nums[0], nums[1]);
            for (int i = 2; i < n; ++i) {
                dp[i] = max(dp[i-2]+nums[i], dp[i-1]);
                    
            }
            return dp[n - 1];
            
            
        }
        int rob(vector<int>& nums) {
            // checks
            if (nums.size() == 0) return 0;
            if (nums.size() == 1) return nums[0];
            if (nums.size() == 2) return max(nums[0], nums[1]);

            int n = nums.size();
            vector<int> nums1(nums.begin(), nums.end()-1);
            vector<int> nums2(nums.begin()+1, nums.end());
            return max(robSubset(nums1),
             robSubset(nums2));
            
            




        }
    };
    