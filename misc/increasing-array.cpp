


















#include <iostream>
#include <bits/stdc++.h>


using namespace std;

int main() {
    int n;
    int x;
    cin >> n;
    vector<int> nums(n);
    for (int i =0; i < n; ++i) {
        cin >> x;
        nums[i] = x;
    }


    long long ans = 0;

    int mx_seen = nums[0];
    vector<int> prefs(n, 0);

    // init maxes
    int i =0;
    while (i < n ) {
        mx_seen = max(mx_seen, nums[i]);
        prefs[i] = mx_seen;
        i++;
    }
    // for (const auto& e : prefs) {
    //     cout << e << " ";
    // }
    // cout << endl;
    //
    int r =0;
    while (r < n) {
        ans += prefs[r] - nums[r];
        r++;
    }
    cout << ans << "\n";

    return 0;


}




















