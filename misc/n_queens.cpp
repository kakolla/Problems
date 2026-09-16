
#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    void place(vector<vector<string>>& ans, vector<string>& board, map<pair<int,int>, int>& bad, 
            int remaining_q, int n) {
        // deep copy
        if (remaining_q == 0) {
            // for (auto e : board) {
            //     cout << e << endl;
            // }
            ans.push_back(board);
            return;
        }

        int i = n - remaining_q;
        // try possible unthreatened spots
            for (int j = 0; j < n; ++j) {
                if (board[i][j] != 'Q' && bad.find(pair<int,int>(i,j)) == bad.end()) {
                    // place
                    board[i][j] = 'Q';
                    


                   // mark unsafe spots
                   vector<pair<int,int>> bad_spots;
                    for (int o = 1; o < n; ++o ) {

                        vector<pair<int,int>> dirs = {
                            {-1, -1}, {-1, 0}, {-1, 1},
                            { 0, -1},           { 0, 1},
                            { 1, -1}, { 1, 0}, { 1, 1}
                        };

                         for (const auto& [dx, dy] : dirs ) {
                            // we are at i,j
                            int nx = i + dx*o;
                            int ny = j + dy*o;
                            if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                                // to back track later
                                bad_spots.push_back(pair<int,int>(nx,ny)); 
                                bad[{nx, ny}]++;
                            }
                        }

                    }
                    place(ans, board, bad, remaining_q-1, n);
                    for (auto p : bad_spots) {
                        bad[{p.first, p.second}]--;
                        if (bad[{p.first, p.second}] == 0) {
                            bad.erase({p.first, p.second});
                        }
                    }
                    board[i][j] = '.';


                }
            }

        



        

    }
    
        
   vector<vector<string>> solveNQueens(int n) {
        // return board soln
        vector<vector<string>> ans;
        if (n == 1) { 
            return vector<vector<string>>({{"Q"}});
        }

        if ( n == 2 || n == 3) return ans;

        map<pair<int,int>, int> bad; // threatened positions

        vector<string> board; // ...., ....,....,.... (dims = n)
        // populate board
        for (int i= 0; i < n; ++i) {

            string line;
            for (int j= 0; j < n; ++j) {
                line += ".";
            }
            board.push_back(line);
        }


        
        // given a board
        // try possible unthreatened spots
        // once all queens placed, if valid, return that board

        place(ans, board, bad, n, n);


        return ans;




        
    }
};
