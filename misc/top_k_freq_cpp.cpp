




#include <bits/stdc++.h>



using namespace std;

class Solution {
public:
    
    vector<int> topKFrequent(vector<int>& nums, int k) {



        unordered_map<int, int> m;

        // freqs
        for (const auto& e : nums) {
            m[e]++;
        }

        // put into freqs
        vector<vector<int>> freqs(nums.size()+1);
        for (const auto [k,v] : m) {
            freqs[v].push_back(k); // freq - > vals that hve this
        }


        // return k most
        int i = nums.size();
        vector<int> ans;
        while (k) {
            if (freqs[i].size()) {
                for (auto e : freqs[i]) {
                    ans.push_back(e);
                    k--;
                }
            }
            i--;
        }
        return ans;
        



        
    }
};





