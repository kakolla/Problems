/* 
Kadane's algorithm:
keep current sum as 0
add current element i to it
if sum ever goes negative, keep track of max sum you've seen so far, and start the next subarray
from the current position i+1
*/

class Solution {
    public:
    
        int maxSubArray(vector<int>& nums) {
            if (nums.size() == 1) return nums[0];
            int ms = 0;
            int max_seen = nums[0];
            for (int i=  0; i < nums.size(); ++i) {
                ms += nums[i];
                max_seen = std::max(max_seen, ms);
                if (ms < 0) {
                    ms = 0;
                }
            }
    
            return max_seen;
            
    
        }
    };
    