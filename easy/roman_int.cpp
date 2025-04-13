#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
    public:

        map<char, int> mp = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int romanToInt(string s) {
            // if less letter comes before big letter
            // subtract
            // if it comes after add
            reverse(s.begin(), s.end());
            
            int size = s.length();
            int num = 0;

            int prev = mp[s[size-1]];
            int cur;
            num += prev;
            for (int i = size-2; i >=0; --i) {
                cur = mp[s[i]];
                if (prev < cur ) {
                    num += (-2 * prev); // subtract
                }
                prev = cur; // update prev
                num += cur; // add normally
            }


            return num;
            



        }
    };

