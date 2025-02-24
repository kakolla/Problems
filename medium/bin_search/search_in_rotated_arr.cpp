/* 
Prob not the most optimal way
but my original approach: find minimum element in rotated arr (logn) -> same as min_in_rotated_arr problem
then binary search both sorted arrays for the target (logn + logn)
total: 3logn

*/

#include <vector>
using namespace std;
class Solution {
    public:
        int binSearch(int l, int r, vector<int> nums, int target) {
            if (l>r) return -1;
    
            int mid = (l+r)/2;
            if (target == nums[mid]) return mid;
            if (target > nums[mid]) {
                return binSearch(mid+1, r, nums, target);
            }
            else {
                return binSearch(l, mid-1, nums, target);
            }
    
        }
    
        int search(vector<int>& nums, int target) {
            int l = 0;
            int r = nums.size() - 1;
            int mid;
    
            // find min's index
            int min = 0;
            while (l <= r) {
                if (l == r) {min = l; break;}
                mid = (l+r)/2;
                if (nums[mid] > nums[r] ) {
                    l = mid+1;
                    min = nums[mid] < nums[min] ? mid : min;
                } 
                else if (nums[mid] < nums[r]) {
                    r = mid;
                    min = nums[mid] < nums[min] ? mid : min;
                }
            }
            
            cout << "min: " << min << endl;
            // not a rotated array
            l = 0;
            r = nums.size() -1;
            cout << min << endl;
                return std::max(binSearch(0, min-1, nums, target), binSearch(min,r, nums, target));
        
    
        }
    };
    