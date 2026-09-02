













#include <bits/stdc++.h>
using namespace std;


int main() {
    int n;
    cin >> n;
    if (n == 2 || n ==3) {cout << "NO SOLUTION" << '\n'; return 0;}

    string ans = "";

    for (int i =2 ; i <= n; i += 2) {
        ans += to_string(i) + " ";
    }
    for (int i = 1 ; i <= n; i += 2) {
        ans += to_string(i) + " ";
    }
    cout << ans << '\n';

    return 0;
}


