
from typing import List
def max_sum(nums: List[int], k):
    # input: nums, k,
    # all inputs positive? sorted?
    # output: max sum of subarray of size k
    
    l = 0 
    r = k-1
    c_sum = sum(nums[:k])
    max_sum = c_sum
    # 0, 3, 7, 13, 11, 17, 0, 10, 0, 4

    for i in range(k, len(nums)):
        # consider the sum when new element enters the window
        # and we delete the leftmost item in window
        curr_sum = c_sum - nums[l] + nums[i]
        c_sum = curr_sum
        max_sum = max(max_sum, curr_sum) # std::max ?
        l += 1
        r += 1
    return max_sum





import random
# arr = [ random.randint(0, 20) for x in range(10)
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]

print(max_sum(arr, 4))