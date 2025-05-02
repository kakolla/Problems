#include <cmath>
#include <iostream>

using namespace std;
class Solution
{
public:
    bool isPalindrome(int x)
    {
        if (x < 0) return false;

        // 101

        // find len of x (string wise)
        int count = 0;
        long temp = x;
        while (temp != 0)
        {
            temp /= 10;
            count++;
        }

        // reverse the number
        long new_num = 0;
        temp = x;
        while (count > 0) {
            int t = temp % 10; // get 1s digit
            new_num += t * pow(10, count-1); // multiply
            temp /= 10;
            count--;

        }
        // cout << new_num << endl;
        
        return new_num == x;
    }
};

// int main()
// {
//     Solution* bread = new Solution();
//     cout << bread->isPalindrome(1234567899);
//     return 0;
// }