



"""
given array of daily stock prices

with only one transaction allowed, find the max profit u can amke by trading stocks

"""

from typing import List
def maxProfit(dailyPrices: List[int]):
    # TODO: single transaction, max profit
    # 3,4,10,3,2,0
    if not dailyPrices: return 0
    max_profit = 0
    l, r = 0, 1
    while r < len(dailyPrices):
        profit = dailyPrices[r] - dailyPrices[l]
        max_profit = max(max_profit, profit)
        if profit < 0:
            l = r
        r += 1
    return max_profit
   

def maxProfitMultiple(dailyPrices):
    # TODO: unlimited transactions, max profit
    # at most one share at a time

    """
        # 3,4,10,3,2, 0, 7, 9, 13

        5 0 30

        3 1 2 7

        1 2 1 2 
    """
    profit = 0
    l, r = 0, 1
    
    accumulated_profit = 0
    while r < len(dailyPrices):
        p = dailyPrices[r] - dailyPrices[l]
        if p <= 0:
            profit += accumulated_profit

            l = r
            accumulated_profit = 0
        else:
            accumulated_profit = p

        r += 1

    profit += accumulated_profit

    return profit








tests = [
    ([1, 2, 3, 5],        4,  4),
    ([5, 3, 2, 1],        0,  0),
    ([7],                 0,  0),
    ([7, 1, 5, 3, 6, 4],  5,  7),
    ([3, 3, 3, 3],        0,  0),
    ([2, 4, 1, 10],       9,  11),
    ([3, 8, 1, 9],        8,  13),
    ([1, 2, 1, 2],        1,  2),
]

for prices, expectedSingle, expectedMultiple in tests:
    resultSingle = maxProfit(prices)
    resultMultiple = maxProfitMultiple(prices)
    statusSingle = "PASS" if resultSingle == expectedSingle else "FAIL"
    statusMultiple = "PASS" if resultMultiple == expectedMultiple else "FAIL"
    print(f"{prices}")
    print(f"  single:   got {resultSingle}, expected {expectedSingle}  [{statusSingle}]")
    print(f"  multiple: got {resultMultiple}, expected {expectedMultiple}  [{statusMultiple}]")
