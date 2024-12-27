/*
Standard intuition: think of backtracking as trying possible solutions
Not sure if this is the most efficient way but yeah
*/



#include <vector>
#include <algorithm>
using namespace std;


class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> soln;

        vector<int> temp; // temporary list
        permuteRecurse(soln, nums, temp, 0, nums.size());
        return soln;
    }

    // check if the temporary vector has duplicate elements
    bool hasNoDupes(vector<int> temp)
    {
        sort(temp.begin(), temp.end());
        for (int i = 0; i < temp.size(); ++i)
        {
            if (i+1 < temp.size())
            {
                if (temp[i] == temp[i+1]) return false;
            }
        }
        return true;
    }

    void permuteRecurse(vector<vector<int>>& soln, vector<int>& nums, vector<int> temp, int pos, int size)
    {
        if (nums.size() == 0) return;
        // base case
        if (hasNoDupes(temp) && pos == size)
        {
            // valid solution
            soln.push_back(temp);
            return;
        }
        if (!hasNoDupes(temp)) return;

        for (int i = 0; i < nums.size(); i++)
        {
            temp.push_back(nums[i]); // explore this solution
            permuteRecurse(soln, nums, temp, pos+1, size);

            temp.pop_back(); // back track
        }
    }
};
