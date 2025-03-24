#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int majorityElement(vector<int>& nums) {
    int size = nums.size();
    
    std::unordered_map<int, int> mp;
    
    // init to 0s
    for (int i = 0; i < nums.size(); ++i) {
        mp[nums[i]] = 0; 
    }

    // count
    for (int i = 0; i < nums.size(); ++i) {
        mp[nums[i]]++; 
    }

    for (const auto& e : mp) {
        if (e.second > size/2) {
            return e.first;
        }
    
    }

    return -1;


}

