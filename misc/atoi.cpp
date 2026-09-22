













#include <bits/stdc++.h>
#include <limits>
using namespace std;

class Solution {
public:
    int myAtoi(string s) {
        int ans = 0;
        int n = s.size();

        // get stripped vresoin
        string temp = "";
        bool lz = true; // leading zero
        bool neg = false;
        bool readint = false;
        for (int i = 0; i < n; ++i) {
            if (lz && s[i] == ' ' && !readint ) continue;
            if (lz && s[i] == '0') {
                readint = true;
                continue;
            }

            if (!readint && s[i] == '-') {
                neg = true;
                readint =true;
                continue;
            }
            if (!readint && s[i] == '+') {
                readint =true;
                continue;
            }

            if (isdigit(s[i])) {
                lz = false;
                readint = true;
                temp += s[i];
            } else break;

        }

        int numdigits = temp.size();
        int j =0 ;
        bool flow = false;
        while (numdigits--) {
            double y = (temp[j] - '0') * (pow(10,numdigits));

            if (y > numeric_limits<int>::max()) {
                ans = neg ? numeric_limits<int>::min() :  numeric_limits<int>::max();
                flow = true;
                break;
            }
            if (ans > numeric_limits<int>::max() - static_cast<int>(y)){
                ans = neg ? numeric_limits<int>::min() :  numeric_limits<int>::max();
                flow = true;
                break;
            }
            ans += static_cast<int>(y);
            j++;
        }
        cout << ans << endl;
        if (!flow && neg) ans *= -1;
        //
        // if (neg && ans == numeric_limits<int>::max()) {
        //     ans = numeric_limits<int>::min() + 1;}
        // else if (neg) ans *= -1;



        return ans;

        // round case
        if (ans < 0 && !neg) {
            // overflow, round
            // 10
            ans = numeric_limits<int>::max();
        } else if (ans > 0 && neg) {
            ans = (1 << 31);
        }

        
        return ans;


        
        

    }
};
