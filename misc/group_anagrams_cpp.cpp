







#include <bits/stdc++.h>


using namespace std;
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
       vector<vector<string>> ans;

        unordered_map<string, vector<string>> m;
       for (auto word : strs) {

           string sw = word;
           sort(sw.begin(), sw.end());
           m[sw].push_back(word);

       }

       // build it back
       for (auto [k,v] : m) {
           ans.push_back(v);
       }

       return ans;
    }
};
