class Solution {
    public:
        vector<vector<int>> generate(int numRows) {  
            vector<int> first = {1};
            vector<int> second = {1, 1};
            vector<vector<int>> ans;
            ans.push_back(first);
            
            if (numRows == 1) return ans;
            ans.push_back(second);
            if (numRows == 2) return ans;       

            for (int i = 2; i < numRows; ++i) {
                vector<int> t;
                t.push_back(1);
                for (int k = 0; k < ans[i-1].size()-1; ++k) {
                    t.push_back(ans[i-1][k] + ans[i-1][k+1]);
                }
                t.push_back(1);
                ans.push_back(t);

            }

            return ans;




        }
    };