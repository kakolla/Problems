/*
https://neetcode.io/problems/daily-temperatures
Key idea here: keep and maintain DECREASING stack
If the current temperature we're looking at when added to stack would make the stack increasing,
i.e. it is greater than the top of stack, go through all elements in stack and update the day "distances"
and then remove them from stack--they're processed.


ex: [2, 1, 1, 3]
2,1,1 is decreasing, but when we add 3
all  elements 2,1,1 share the next increasing daily temperature as 3, so we can update 2,1,1 indices to be consider 3.
*/



#include <vector>
#include <string>
#include <stack>


using namespace std;
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> result(temperatures.size());



        // goal is to create a monotonically decreasing stack
        stack<pair<int,int>> st;
        // pair<index, value>

        st.push(pair<int, int>(0, temperatures[0]));

        for (int i = 1; i < temperatures.size(); ++i)
        {
            int elem = temperatures[i];

            // compare to top of stack
            pair<int, int> top = st.top();
            

            while (!st.empty() && elem > top.second)
            {
                
                // violates decreasing stack
                // so update top element (in stack) day count
                result[top.first] = i - top.first;
                st.pop();
                if (!st.empty())
                {
                    top = st.top();
                }
            }
        
            st.push(pair<int, int>(i, elem));

        }

        return result;
    }
};
