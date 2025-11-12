"""
we can compute the differences of costB and costA,
sort this (greedy)
and then this represents a preference of where this person should go
tally up cost sending lower n to city B, upper n to city A
"""
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # o: min cost to fly every person to a city s.t half are in both cities
        n = len(costs) // 2 

        # calc diffs
        diffs = [0] * 2 * n
        i = 0

        for cost_a, cost_b in costs:
            diffs[i] = (cost_b - cost_a, i)
            i += 1
        print(diffs)
        diffs.sort()

        # tally up costs
        # lower n will be ppl who should go to B (neg diffs)
        # upper n will be those who should go to A (pos diffs)
        min_cost = 0
        for i in range(n):
            p = diffs[i][1]
            min_cost += costs[p][1]
        for i in range(n, 2*n):
            p = diffs[i][1]
            min_cost += costs[p][0]
        
        return min_cost