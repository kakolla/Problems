

















#include <iostream>

using namespace std;
int main() {
    // n(n+1)/2
    long long s;
    
    int n;
    cin >> n;

    int t;

    s = 1LL * n * (n+1)  / 2;
    n--;
    while (n--) {

        cin >> t;
        s -= t;
    }
    cout << s;






    return 0;
}
