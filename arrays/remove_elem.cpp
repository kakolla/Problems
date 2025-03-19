class Solution {
    public:
        int removeElement(vector<int>& nums, int val) {
            if (nums.size() == 0) return 0;
            // mark as removed
            for (int i = 0; i < nums.size(); ++i) {
                if (nums[i] == val) {
                    nums[i] = -1;
                }
            }
    
            // bring non removed elements to front
            for (int i = 0; i < nums.size(); ++i) {
                if (nums[i] == -1) {
                    for (int k = i; k < nums.size(); ++k) {
                        if (nums[k] != -1) {
                            std::swap(nums[i], nums[k]);
                            break;
                        }
                    }
    
                }
            }
            
            // count 
            int s = 0;
            for (int i = 0; i < nums.size(); ++i ) {
                if (nums[i] == -1) {
                    break;
                }
                s++;
            }
            return s;
            
        }
    };