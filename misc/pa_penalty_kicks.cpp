/*
   https://contest.usc.edu/pmwiki.php/Main/Spring26?action=download&upname=spring2026.pdf
   problem a
*/













#include <bits/stdc++.h>
using namespace std;




// max p the goakeep ercan ave teh shot, choose the best spot



int main() {
    int k, h, w;
    double val;

    cin >> k;


    vector<tuple<int,int>> dirs = {
        {0,1},
        {0, -1},
        {1,0},
        {1,1},
        {1,-1},
        {-1,0},
        {-1,1},
        {-1,-1}
    };


    int nx, ny;

    double p;

    int t = 1;
    while (k--) {

        cin >> h >> w;
        vector<vector<double>> grid(h, vector<double>(w, 0));
        double max_p = 0;
        for (int i = 0; i < h; ++i) {
            for (int j = 0 ; j < w; ++j) {
                cin >> val;
                grid[i][j] = val;
            }
        }



        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                p = grid[i][j];
                for (auto& [dx,dy] : dirs) {
                    nx = i + dx, ny = j + dy;
                    if (0 <= nx && nx < h && 0 <= ny && ny < w) {
                        p += grid[nx][ny] * 0.5;
                    }
                }
                max_p = max(max_p, p);

            }

        }

        cout << "Data Set " << t << ":" << '\n';
        cout << max_p << '\n';
        cout << '\n';


        t++;

    }


}




