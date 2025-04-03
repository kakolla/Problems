class Solution {
    public:
        int maxProfit(vector<int>& prices) {
            
            int l = 0;
            int max = 0;
            for (int r = 1; r < prices.size(); ++r) {
                while (prices[r] < prices[l]) {
                    l++;
                }
                max = std::max(max, prices[r] - prices[l]);

            }
            return max;


            
        }
    };