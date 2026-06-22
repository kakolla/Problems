


#include <string>
#include <unordered_map>

using namespace std;
class Solution {
public:
    int maxNumberOfBalloons(string text) {
	    int nb = 0;
	    string balloon = "balloon";
	    typedef unordered_map<char, int> map;

	    map mp;
	    for (const char& e : text) {
		    mp[e]++;
	    }
	    bool flag = true;
	    while (flag){
		    for (const char& c : balloon) {
			    if (mp[c] == 0) {
				    flag = false;
				    break;
			    }
			    mp[c] --;
		    }
		    if (!flag) break;
		    nb++;
	    }
	    return nb;
        
    }
};      
