from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:

        

        # guaranteed to hit end
        # basically like a look ahead 2 greedy algo

        steps = 0

        i = 0 # pos
        end = 0 # where we can reach from this current jump

        furthest = 0 # furthest possible reach (2nd jump ahead)

        # [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]

        while i < len(nums) - 1:
            furthest = max(furthest, i + nums[i])

            if i == end:
                steps += 1
                # now we can search up to furthest
                end = furthest
            i += 1

        return steps



