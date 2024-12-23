/*
Two pointers approach (left and right pointer)
Using cases decide which pointer to advance
*/

#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;
        while (l < r)
        {
            int sum = numbers[l] + numbers[r];
            if (sum == target)
            {
                return vector<int> {l+1, r+1};
            }
            else if (sum > target)
            {
                r--;

            }
            else if (sum < target)
            {
                l++;
            }
        }
        return vector<int>();

    }
};
