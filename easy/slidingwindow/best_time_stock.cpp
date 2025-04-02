class Solution {
    public:
        int maxProfit(vector<int>& prices) {
            int s = prices.size();

            
            int l =0;
            int r = 0;
            int p = 0;
            for (int i = 1; i < s; ++i) {
                // if day's price goes down our left
                // l should point to lowest price we've seen
                if (prices[i] < prices[l]) {
                    // l++; no
                    l = i;
                }
                // calc curr profit
                int t = prices[i] - prices[l];

                // update if better profit
                if (t > p) {
                    p = t;
                }
             


            }
            return p;                  
                
        }
    };