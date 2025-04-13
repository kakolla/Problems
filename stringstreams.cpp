#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    string input = "1,3, abhi, yeah";
    stringstream ss(input);
    string temp;
    
    
    
    while (getline(ss,temp, ',')) {
        cout << temp << endl;


    }


    return 0;
}