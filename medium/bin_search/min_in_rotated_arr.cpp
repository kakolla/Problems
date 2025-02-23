// rotated array has two fragments: sorted_left and sorted_right
// find the min (first of right sorted_right) with bin search
#include <vector>
using namespace std;
class Solution {
public:

    int binSearch(int l, int r, int s, vector<int>& nums) {
        
        int mid;
        int min = nums[0];
        while (l <= r) {
            if (l == r) return nums[l];
            mid = (l+r)/2;
            
            // if mid val is greater than the right index, the min should b to the right
            if (nums[mid] > nums[r]) {
                l = mid+1;
                min = std::min(nums[mid], min);
            } 
            else {
                r = mid;
                min = std::min(nums[mid], min);
            }
        }
        return min;
    }
    int findMin(vector<int> &nums) {
        return binSearch(0, nums.size()-1, 1000, nums);
        
    }
};
