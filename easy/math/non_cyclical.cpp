class Solution {
    public:
        bool isHappy(int n) {
    
            set<int> seen;
            while (1) {
                int sum = 0;
                string s = to_string(n);
                for (int i= 0; i < s.size(); ++i) {
                    sum += pow(s[i] - '0', 2);
                }
                cout << sum << endl;
                if (sum == 1) return true;
                if (seen.find(sum) != seen.end()) return false; // cycle
                seen.insert(sum);
                n = sum;
    
    
    
            }
            
        }
    };
    