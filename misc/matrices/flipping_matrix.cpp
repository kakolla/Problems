/*
Trick is that you don't need to brute force reverse every col and row
just iterate over the square n and find the mirrored (2 * n - r -1), etc values and find the max of those

*/

#include <vector>

using namespace std;
int flippingMatrix(vector<vector<int>> matrix) {
    int n = matrix.size() /2;
    
    int max_sum = 0;
    int max_elem = -1;
    for (int r = 0; r < n; ++r) {
        for (int c=  0; c < n; ++c) {
            int curr = matrix[r][c];
            max_elem = max({curr, matrix[r][2*n-c-1],
            matrix[2*n-r-1][c], matrix[2*n-r-1][2*n-c-1]});
            
            max_sum += max_elem;
            
        }
    }
    return max_sum;

}