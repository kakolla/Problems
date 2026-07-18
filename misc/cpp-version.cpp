













#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {

        vector<int>::iterator beg = nums.begin();
        vector<int>::iterator end = nums.begin() + k;

        vector<int> subs(beg, end);
        priority_queue<int, vector<int>, greater<int>> pq(subs.begin(), subs.end());

        for (int i = k; i < nums.size(); ++i) {
            pq.push(nums[i]);
            pq.pop();
        }
        return pq.top();


        
    }
};

