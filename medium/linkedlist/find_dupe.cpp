
/*
og thinking:
hashmap but not O(1) space
*/

/*
approach:
use array itself
since vals are valid indices
loop through array, hop to the element by curr index,
mark as negative
if you come across a neg number, it is a dupe

*/


class Solution {
    public:
        int findDuplicate(vector<int>& nums) {
            


            // since all vals contain vals that are valid indices
            // we can mark those positions with *-1
            // if theres a dupe, we encounter a -1 in for loop
            for (int i = 0; i < nums.size(); ++i) {
                if (nums[abs(nums[i])-1] < 0) return abs(nums[i]);
                nums[abs(nums[i]) - 1] *= -1;
                // subtract 1 because range is [1,n]
                // not [0, n]
            }
            




        }
    };
    