#include <string>

using namespace std;

class Solution {
    public:
        string longestPalindrome(string s) {
        int resultLen = 0;
        int resultStart = 0;

        // d(i-1, j+1) = s[n-1] + d(i, j) + s[n+1] ?
        for (int i= 0; i < s.size(); ++i) {
            int l = i, r = i;
            // check for odd length palindrome (i-1, r+1)
            while (l>= 0 && r < s.size()) {
                if (s[l] == s[r]) {
                    int tempLen = r - l + 1;
                    if (tempLen > resultLen) {
                        resultStart = l;
                        resultLen = tempLen;
                      
                    }
                    l--;
                    r++;
                } else break;

            }            

            // check for even length palindrome
            l = i;
            r = i+1;
            if (r >= s.size()) continue;
            while (l >= 0 && r < s.size()) {
                if (s[l] == s[r]) {
                    int tempLen = r-l + 1; // 1 character has same index, add 1
                    if (tempLen > resultLen) {
                        resultStart = l;
                        resultLen = tempLen;      
                    

                    } 

                    l = l-1;
                    r = r+1;
                    
                } else break;


            }


        }
               
            return s.substr(resultStart, resultLen);



        }
        
    };
    