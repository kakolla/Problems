


"""
spent like a good 20 min thinking baout it 
 - visualize it like a bar chart
- no point in selling and buying on the same day, because its equivalent to just keeping it

- so we sell IF our potential profit went down from what we could've made yesterday ; so we need a seen profit that is delayed
- keep increasing if it's better, if it went down from what we saw, add what we saw (as if we sold eysterday)and buy today 

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit across multiple days  
        maxprofit = 0
        seenprofit = 0
        profit = 0

        l, r = 0, 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < seenprofit:
                # if profit dips down
                maxprofit += seenprofit
                l = r
                seenprofit = 0
            else:
                seenprofit = profit
            r += 1
        maxprofit += seenprofit
        return maxprofit


