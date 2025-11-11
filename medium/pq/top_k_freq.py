class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) +1
        from collections import defaultdict
        f = defaultdict(int)
        for l in nums:
            f[l] += 1
        
        # get map of 
        # frequency -> list of elements
        m = defaultdict(list)
        for l,f in f.items():
            m[f].append(l) # get letters that have this frequency

        # we could build freqs and sort O(nlogn)
        # or since there's max n letters, use an array O(n)
        arr = [[] for i in range(n)]
        
        for f, elems in m.items():
            arr[f] = elems
        
        print(arr)
        # walk backwards
        ans = []
        i = n-1
        while len(ans) < k and i >= 0:
            if arr[i]:
                ans.extend(arr[i])
            i -= 1
        return ans[:k]

