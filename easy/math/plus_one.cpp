class Solution {
    public:
        vector<int> plusOne(vector<int>& digits) {
            int size = digits.size();
            int i = size-1;
            while (true) {
                if (i < 0) break;
                if (digits[i] < 9) {
                    digits[i]++;
                    break;
                }
                else {
                    digits[i] = 0;
                    i--;
                }            
            }
            // worst case
            if (digits[0] == 0) {
                digits.insert(digits.begin(), 1);
            }
            return digits;
            
        }
    };
    