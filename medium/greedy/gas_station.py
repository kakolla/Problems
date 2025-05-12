# greedy approach
# if curr_gas goes negative, that means the next possible candidate is i+1
# and there is guaranteed a soln (ruled out no solution as a possibility) in the future,
# so i+1 should be it or a future soln

from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # not enough gas to cover the cost
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)

        # gauranteed to have at most one solution here
        curr_gas = 0
        index = 0 # index to return
        for i in range(n):
            curr_gas += gas[i] - cost[i] # accumulate gas
            if curr_gas < 0:
                # if neg, reset
                curr_gas = 0
                index = i+1
                if index >= len(gas):
                    index = index % len(gas)
                print(index)
        
        return index

        