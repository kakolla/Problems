from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sums = [0 for i in range(len(gain) +1)]

        sum = 0
        highest = 0
        for i in range(len(gain)+1):
            prev = gain[i-1] if i-1 >=0 else 0
            prefix_sums[i] = prev + sum
            sum += prev
            highest = max(highest, sum)
        
        print(prefix_sums)
        return highest






        