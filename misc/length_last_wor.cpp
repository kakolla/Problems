









#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    int lengthOfLastWord(string s) {
        string curr = "";

        for (int i = s.size() -1; i >= 0; --i) {

            if (s[i] != ' ') {
                curr += s[i];
            } else if (curr.size() == 0 && s[i] == ' ') {
                continue;
            }
            else {
                return curr.size();
            }



        }
        return curr.size();
        
    }
};



