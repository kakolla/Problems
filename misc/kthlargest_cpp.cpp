
#include <bits/stdc++.h>

using namespace std;
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {

        priority_queue<int, vector<int>, greater<int>> pq;
        int max_val = 0;
        for (const auto& e : nums) {
            pq.push(e);
            if (pq.size() == k+1) {
                pq.pop();
            }

        }

        return pq.top();
        
    }
};





