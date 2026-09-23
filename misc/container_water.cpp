













#include <bits/stdc++.h>
using namespace std;



class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_area = numeric_limits<int>::min();


        int l = 0, r = height.size()-1;

        int s;
        int a;
        while (l < r) {
            s = min(height[l], height[r]);
            a = s * (r-l);
            max_area = max(max_area, a);
            if (height[l] == s) l++;
            else if (height[r] == s) r--;

            
        }
        return max_area;



        
    }
};
