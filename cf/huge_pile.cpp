
#include <iostream>
#include <cmath>
#include <unordered_map>


using namespace std;

static unordered_map<string, int> cache;

int bs(long long n, long long k) {
    if (n == k) return 0;
    if (n < k) return -1;

    double c = (double)n/2;
    long long b1 = std::floor(c) ;
    long long b2 = std::ceil(c);
    // printf("n=%lld, time=%d\n",n, time);


    int exp1;
    int exp2;
    // check if cached else recurse
    if (b1 == b2) {
        auto it = cache.find(to_string(b1) +',' + to_string(k));
        if (it != cache.end()) {
            return it->second == -1 ? -1 : 1 + it->second ;
        } else {
            int res = bs(b1, k);
            cache[to_string(b1) +',' + to_string(k)] = res;
            return res == -1 ? -1 : 1 + res;

        }

    }
    else {
        string t1 = to_string(b1) +',' +  to_string(k);
        auto it1 = cache.find(t1);
        string t2 = to_string(b2) + ',' + to_string(k);
        auto it2 = cache.find(t2);
        if (it1 != cache.end()) {
            exp1 = cache[t1] == -1 ? -1 : 1+ cache[t1];
        }
        else  {
            exp1 = bs(b1, k);
            cache[t1] = exp1;
            if (exp1 != -1) exp1++;
        }

        if (it2 != cache.end()) {
            exp2 = cache[t2] == -1 ? -1 : 1 + cache[t2];
        } else  {
            exp2 = bs(b2, k);
            cache[t2] = exp2;
            if (exp2 != -1) exp2++;
        }

    }

    if (exp1 == -1 && exp2 == -1) return -1;
    if (exp1 == -1) return exp2;
    else if (exp2 == -1) return exp1;
    else return min(exp1, exp2);

}
int main() {
    int t;
    cin >> t;

    long long n, k;
    int res;
    for (int i= 0;i<t; i++) {
        cin >> n >> k;


        string s = to_string(n) + ',' + to_string(k);
        auto it = cache.find(s);
        if (it != cache.end()) {
            res = it->second;
        }
        else  {
            res = bs(n, k);
            cache[s] = res;
        }
        cout << res << '\n';


    }
    

    

    return 0;
}
