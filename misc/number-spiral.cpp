/* 
 * just stare at the matrix long enough
 *
 * 1   2   9  10  25
4   3   8  11  24
5   6   7  12  23
16  15  14  13  22
17  18  19  20  21
 *
 * pattern is to see the diagnol value can be calculoted easily, and based on 
 * direction we can add or subtract form there
 *
 * */


#include <bits/stdc++.h>
using namespace std;


int main() {
    int t;
    cin >> t;
    long x, y;   
    long diag;

    long dx; // how much to sub/add from the diag value
    

    long diagval;
    for (int i = 0;i < t; ++i) {
        cin >> x >> y;
        x -= 1;
        y -= 1;
        if (x == 0 && y == 0) {
            cout << 1 << '\n';
            continue;
        }
        diag = max(x, y); // take max ie (3, 3)
        // diagonol num
        // from a diag num, we are moving into it and out (alternating directions)

        // 0 - 1
        // 1 - going down and left (incr)
        // 2 - right and going up
        // 3 - going down and left

        // n^2 + n + 1
        diagval = diag * diag + diag + 1;
        if (diag % 2 == 1) {
            // down and left
            if (diag == x) {
                //match row  
                dx =  (diag - y);
            } else {
                // matches col
                dx = -1 * (diag - x);
            }
            diagval += dx;

        } else {
            // right and up
            if (diag == x) {
                // column
                dx = -1 *  (diag - y);
            } else {
                // matches row
                dx = (diag - x);
            }
            diagval += dx;
        }
        cout << diagval << '\n';

    }


    return 0;
}


