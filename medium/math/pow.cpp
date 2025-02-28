// raise x^n without library, n is an integer


class Solution {
    public:
    
        double myPow(double x, int n) {
            if (n == 0) return 1;
            if (n == 1) return x;
            double pos = n > 0 ? 1 : 0;
            n = n > 0 ? n : -1* n;
            double p = x;
            for (int i = 1; i < n; ++i) {
                p *= x;
            }
            if (pos) {
                return p;
            } else {
                return 1/p;
            }        
            
        }
    };
    