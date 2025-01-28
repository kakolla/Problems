#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string timeConversion(string s) {
    string a_or_p(1, s[8]);
    int hour;
    char h[3];
    h[2] = '\0';
    if (a_or_p == "A")
    {
        h[0] = s[0];
        h[1] = s[1];
        hour = ((h[0]-'0') * 10 + (h[1]-'0')) % 12;
    }
    else if (a_or_p == "P")
    {
        h[0] = s[0];
        h[1] = s[1];
        hour = ((h[0]-'0') * 10 + (h[1]-'0')) % 12 +12; 
    }
    string ans = s.substr(0,8);
    ans[0] = char(hour/10 + '0');
    ans[1] = char(hour % 10 + '0');
    
    return ans;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
