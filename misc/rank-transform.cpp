











#include <bits/stdc++.h>

#define map unordered_map<int,int>

using namespace std;
class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        vector<int> ans;
        set<int> s(arr.begin(), arr.end());


        map mp;
        int i = 0;
        for (auto& e : s) {
            cout << e << endl;
            mp[e] = i;
            i++;
        }
        for (auto& e : arr) {
            ans.push_back(mp[e]+1);
        }
        return ans;
    }
};
