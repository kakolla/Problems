/*
Store a variable max reach, and you greedily choose the furthest 
pos you can jump (which is position + max jump).
if a section in the array (i) is not reachable (less than max reach), you cant reach the end


*/

class Solution {
    public:
        bool canJump(vector<int>& nums) {
            if (nums.size() == 1) return true;
            int l = nums.size() - 1;
    
            // max reach can be determined as i (position) + max jump (nums[i])
            // if max reach extends or equals last pos, we can reach the last index
            int max_r = 0;
            for (int i = 0; i < nums.size(); ++i) {
                if (i > max_r) return false; // this index cannot be reached (max reach doesnt get there)
    
                if (max_r >= l) return true;
                max_r = std::max(max_r, i + nums[i]);
    
                
            }
            return false;
    
        }
    };
    