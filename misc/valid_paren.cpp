



#include <bits/stdc++.h>



using namespace std;


class Solution {
public:
    bool isValid(string s) {
	    stack<char> st;

	    int i;
	    int n = s.size();


	    map<char, char> cr = {
            {'{', '}'},
            {'(', ')'},
            {'[', ']'},
	    };


        char top;


        for (char curr : s) {
            if (cr.find(curr) != cr.end()) {
                st.push(curr);
            }

            else {
                // close bracket
                if (st.empty()) return false;
                char top = st.top();
                if (curr != cr[top]) return false;

                st.pop();
            }



        }

        return st.empty();



		







	    
        
    }
};
