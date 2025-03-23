// https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75


class Solution {
    public:
        string mergeAlternately(string word1, string word2) {
            int i = 0;
            int t = 0;
            string str = "";
            int smallest = std::min(word1.length(), word2.length());
            while (i < smallest) {
                if (t == 0) {
                    str += word1[i];
                }
                else if (t == 1) {
                    str += word2[i];
                }
                t++;
                if (t == 2) {
                    t = 0;
                    i++;
                }
            }
    
            if (word1.length() == word2.length()) return str;
            // append onto end of merged string
            string trail = i < word1.length() ? word1 : word2;
            for (int m = i; m < trail.length(); ++m) {
                str += trail[m];
            }
            return str;
            
        }
    };