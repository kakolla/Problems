
from typing import List
def top_k_freq_elems(nums: List[int], k):
    # input: num list
    # output: k most freq items
    # sorted data? - must be better tha nlogn

    # 2 most freq items
    # 3 most freq items ...

    # base /edge cases TODO

    # store in dict
    # iterate and store in PQ 
    mp = {}
    for x in nums:
        mp[x] = mp.get(x, 0) + 1 # increment count
        
    
    import heapq
    heap = []
    for key, val in mp.items():
        heapq.heappush(heap, (-val, key)) # value is the freq


    ans = []
    for l in range(k):
        ans.append(heapq.heappop(heap)[1]) # gets the count

    return ans
        

nums = [1,1,1,2,2,3]
k = 2
print(top_k_freq_elems(nums, k))

