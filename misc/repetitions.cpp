















#include <iostream>
#include <string>


using namespace std;
int main() {


    string s;
    getline(cin, s);
    int l = 0, r = 1;

    int mx_rep = 1;
    int ln = s.size();

    char curr_char = s[0];
    int cur = 1;
// ATTCGGGA
    while (r < ln) {
        if (s[r] == curr_char) {
            r++;
            cur++;
            mx_rep = max(mx_rep, cur);
        } else {
            l = r;
            r++;
            cur = 1;
            curr_char = s[l];
        }


    }
    

    cout << mx_rep;
    









    return 0;
}
