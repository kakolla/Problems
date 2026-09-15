











#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // do a pass

        // see if k-1 exists, start tracking 

        unordered_set<int> s;
        for (auto e : nums) {
            s.insert(e);
        }
        
        int lcs = 0;
        for (auto e : s ) {
            if (s.find(e-1) == s.end()) {
                // start sequence
                int j = e+1;
                int z = 1;
                while (s.find(j) != s.end()) {
                    z++;
                    j++;
                }
                lcs = max(lcs, z);

            }


        }
        return lcs;


        
        
    }
};
