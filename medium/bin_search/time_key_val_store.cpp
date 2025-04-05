#include <unordered_map>
#include <vector>

using namespace std;

class TimeMap {
    public:
        unordered_map<string, vector<string>> vals;
        unordered_map<string, vector<int>> stamps;
        TimeMap() {
            

        }
        
        void set(string key, string value, int timestamp) {
            // vals[key] = value;
            vals[key].push_back(value);
            stamps[key].push_back(timestamp);

        }
        
        string get(string key, int timestamp) {
            if (vals.find(key) == vals.end()) {
                return "";
            }

            vector<int> vect = stamps[key];

            // indices
            int l = 0;
            int m;
            int r = vect.size()-1;
            while (l <= r) {
                m = (l+r)/2;
                if (vect[m] == timestamp) return vals[key][m];
                if (vect[m] < timestamp) {
                    l = m+1;
                } else {
                    r = m-1;
                }
            }
            if (r < 0) {
                return "";
            }
            return vals[key][r];

          


        }
    };
    