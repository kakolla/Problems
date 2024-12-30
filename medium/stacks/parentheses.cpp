/*
Use backtracking along with stack 
stack is used to keep track of # of brackets since we have a limited amount to use
*/

#include <vector>
#include <string>
#include <stack>

using namespace std;
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> sol;


        // keep stacks of open and closed parantheses
        stack<string> stopen;
        stack<string> stclose;

        // populate them
        for (int i = 0; i < n; ++i)
        {
            stopen.push("(");
            stclose.push(")");
        }
        
        recurse(n, 0, sol, stopen, stclose, string(""), 0, 0);
        return sol;
    }

    void recurse(int n, int x, vector<string>& sol, stack<string> stopen, stack<string> stclose, string temp, int open, int close)
    {
        // if we go past the end
        if (x > n*2-1) return;

        // explore solution: (
        string temp2 = temp;
        if (close <= open+1 && !stopen.empty())
        {
            string bracket = stopen.top();
            temp += bracket;
            stopen.pop();
            recurse(n, x+1, sol, stopen, stclose, temp, open+1, close);
            stopen.push(bracket);

        }

        // explore solution: )
        if (close+1 <= open && !stclose.empty()) // pruning: ignore recursive calls that are obviously wrong
        {
            string bracket = stclose.top();
            temp2 += bracket;
            stclose.pop();
            recurse(n, x+1, sol, stopen, stclose, temp2, open, close+1);
            stopen.push(bracket);
        }


        if (x == n*2-1) // if position is at the end (double of num of pairs)
        {
            cout << "adding " << temp << endl;
            sol.push_back(temp2); // add to solution
            return;
        } 
    }
};
