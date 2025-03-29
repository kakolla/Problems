class Solution {
    public:
        vector<int> getRow(int rowIndex) {
            vector<int> curr;
            curr.push_back(1);
            if (rowIndex == 0) return curr;
            
            curr.push_back(1);
            if (rowIndex == 1) return curr;
            
            for (int i = 1; i < rowIndex; ++i) {
                vector<int> nw;
                nw.push_back(1);
                for (int k = 0; k < curr.size() -1; ++k) {
                    nw.push_back(curr[k] + curr[k+1]);
                }
                nw.push_back(1);
                if (i == rowIndex) return nw;
                curr = nw;
            }


            return curr;

        }
    };