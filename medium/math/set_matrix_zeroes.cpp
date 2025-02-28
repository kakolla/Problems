/*
basically brute force 
*/

class Solution {
    public:
        void set(vector<vector<int>>& matrix, int r, int c) {
            // set all in row to 0
            for (int k = 0; k < matrix[0].size(); ++k) {
                matrix[r][k] = 0;
            }
            // set in col to 0
            for (int k = 0; k < matrix.size(); ++k) {
                matrix[k][c] = 0;
            }
        }
    
        void setZeroes(vector<vector<int>>& matrix) {
            if (matrix.size() == 0) return;
            int size = matrix.size();
            vector<std::pair<int, int>> m;
            for (int i = 0; i < matrix.size(); ++i ) {
                for (int j = 0; j < matrix[i].size(); ++j ) {
                    if (matrix[i][j] == 0) {
                        m.push_back(pair<int, int>(i, j));
                        // set(matrix, i, j);
                        // this is the problem, don't set 0s as iterating
                    }
                }
            }
            for (auto elem : m) {
                cout << elem.first << endl;
                set(matrix, elem.first, elem.second);
            }
            
        }
    };
    