"""
keep track of prefix sum, which just tracks the positions of edges
then use that and logic what would get min slices
"""
from typing import List
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # o: min number of crossed bricks

        # create a prefix sum, places where there r crossings
        n = len(wall)
        prefix_sums = []
        for row in wall:
            s = 0
            prefix_sums.append([])
            count = 0
            for v in row:
                s += v
                if count != len(row)-1:
                    prefix_sums[-1].append(s)
                count += 1
            
        # check prefix sums, count how many edges we have for that 
        # index
        from collections import defaultdict
        c = defaultdict(int)
        for row in prefix_sums:
            for val in row:
                c[val] += 1 # incr count
        
        # min number of slices is index with most edges
        max_edges = -float('inf')
        min_slices = float('inf')
        for k, v in c.items():
            if v > max_edges:
                min_slices = k
                max_edges = v
            
        if not c: # edge case: all bricks size 1, then
            return n
        else:
            return n-max_edges