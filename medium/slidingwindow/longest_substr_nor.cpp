/*
Solved without any help 🙏
sliding window technique
    if a new char enters window and causes there to be a dupe
        subtract left (reduce window) and update map 
        and keep track of max length seen
only thing to be careful is how c++ substr() works
it is (start_pos, length) not (start, end)
*/

#include <unordered_map>

#include <string>
using namespace std;
class Solution {
    public:

        bool check_dupe(char c, unordered_map<char, int>& mp) {
            return mp[c] > 1;
        }

        int lengthOfLongestSubstring(string s) {
            if (s.length() == 0) return 0;
            if (s.length() == 1) return 1;


            unordered_map<char, int> mp;
            int len = 0; // length
            
            
            int l = 0;
            for (int i=0; i < s.size(); ++i) {
                char cur = s[i];
                mp[s[i]]++;
                while (check_dupe(cur, mp) ) {
                    mp[s[l]] -= 1;
                    l++;
                }
                 
                // substr uses (start_pos, LENGTH)
                int temp_length = s.substr(l,i-l+1).length();
                cout << temp_length << endl;
                len = max(len, temp_length);
                


            }

            return len;



            



        }
    };
    