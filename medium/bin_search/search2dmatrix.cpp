/*
https://neetcode.io/problems/search-2d-matrix
Just binary search search twice
Trick here is once you exit out of row binary search loop, subtract 1 for the row index to be searched for cols
Gotta worry about index validity / edge cases
*/
#include <vector>


using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // search rows first
        int bottom = 0;
        int top = matrix.size()-1;
        int mid;
        while (bottom <= top)
        {            
            mid = (top + bottom) / 2;
            if (matrix[mid][0] == target) return true;
            if (matrix[mid][0] > target)
            {
                top = mid-1;
            }
            else if (matrix[mid][0] < target)
            {
                bottom = mid+1;
            }
            
        }

        // have to subtract 1 because last loop exits when bot > top
        int ri = bottom - 1; // this is the row index

        if (ri < 0 || ri >= matrix.size()) return false; // check if ri is invalid

        // now binary search in columns
        bottom = 0;
        top = matrix[ri].size()-1;
        while (bottom <= top)
        {            
            mid = (top + bottom) / 2;
            if (matrix[ri][mid] == target) return true;
            if (matrix[ri][mid] > target)
            {
                top = mid-1;
            }
            else if (matrix[ri][mid] < target)
            {
                bottom = mid+1;
            }
            
        }
        return false;
    }
};
