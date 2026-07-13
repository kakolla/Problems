













#include <bits/stdc++.h>
using namespace std;


class RecentCounter {
public:
    vector<long long> q;

    RecentCounter() {
        this->q = vector<long long>();
        
    }
    
    int ping(int t) {
        // return num of reqs in [t-3000, t]
        int nr = 0;
        this->q.push_back(t);

        int r = this->q.size()-1;
        long long top;
        while (r >= 0) {
            top = this->q[r];
            if (top >= t - 3000 ) {
                nr++;
                r--;
            }
            else break;
        }
        return nr;

        
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
