









#include <bits/stdc++.h>



using namespace std;

class Solution {
public:
    void merge(vector<int>& nums, int l, int r) {
        if (l >= r) return;

        int m = (l) + (r-l)/2;
        merge(nums, l, m);
        merge(nums, m+1,r);

        // merge
        // 2 3 7   1 4 6
        // 1 3 7   2 4 6 
        // 1 2 3   7 4 6
        int a = l , b = m+1;
        while ( a <= m && b <= r) {
            if (nums[b] < nums[a]) {
                int val = nums[b];
                int index = b;

                // shift to right

                while (index != a) {
                    nums[index] = nums[index-1];
                    index--;
                }
                // once we hit here, put the smaller elem here
                nums[a] = val;
                a++;
                m++;
                b++;
            }
            else a++;
        }


    }
    void sortColors(vector<int>& nums) {
        int n = nums.size();

        // rwb
        // same color are adject, with order R W B
        // R - 0, W - 1, B - 2
        //

        merge(nums, 0, nums.size()-1);

        



        
    }
};


