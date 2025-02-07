/*
Original intuition: 
start at a wall, then move forward till you find another wall 
that is greater in height, then calc this running sum. then skip to that wall, and keep going.
Problem w/ this: it is O(n) but doesn't look at max height walls happening before

Strategy: use prefix MAX array and suffix MAX array to get quickly the max height at a location
then add the running sum. ez
*/


#include <vector>

using namespace std;
class Solution {
public:
    int trap(vector<int>& height) {
        // compute prefix maximums first
        vector<int> prefix_max(height.size(), 0);
        int curr_max = height[0];
        for (int i= 0; i < height.size(); ++i)
        {
            prefix_max[i] = std::max(curr_max, height[i]);
            if (height[i] > curr_max) curr_max = height[i];
        }

         // compute postfix maximums
        vector<int> postfix_max(height.size(), 0);
        curr_max = height[height.size()-1];
        for (int i= height.size()-1; i >=0; i--)
        {
            postfix_max[i] = std::max(curr_max, height[i]);
            if (height[i] > curr_max) curr_max = height[i];
        }

        // iterate thru array calcing running sum
        // since bars represent width 1, can just add the heights of water
        int sum = 0;
        for (int i = 0; i < height.size(); ++i)
        {
            sum += std::min(prefix_max[i], postfix_max[i]) - height[i];
        }
        
        return sum;
    }
};
