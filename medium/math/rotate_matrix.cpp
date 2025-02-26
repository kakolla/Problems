/*
To rotate right 90 degrees, transpose matrix then flip cols
*/

class Solution {
    public:
        void rotate(vector<vector<int>>& matrix) {
            int s = matrix.size()-1;
            
            // transpose the matrix
            for (int i = 0; i < matrix.size(); ++i)
            {
                for (int j = i+1; j < matrix[i].size(); ++j) {
                    // 0, 2 => 2,0
                    std::swap(matrix[i][j], matrix[j][i]);
                }
            }
    
            // flip the cols
            for (int i= 0; i < matrix.size(); ++i) {
                std::reverse(matrix[i].begin(), matrix[i].end());
                // for (int j = 0; j < matrix[i].size(); ++j) {
                //     std::swap(matrix[i][j], matrix[s-i][s-j]);
                // }
            }
            
        }
    };
    