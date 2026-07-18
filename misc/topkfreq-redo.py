











class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most frequent elements
        t = len(nums)
        from collections import defaultdict
        m = defaultdict(int)

        for n in nums:
            m[n] += 1
        # group by freqs
        freqs = [[] for _ in range(t+1)]
        print(freqs)

        print(m)
        for n, freq in m.items():
            freqs[freq].append(n)

        print(freqs)
        r = t
        c = 0
        ans = []
        print('--')
        while c < k and r >= 0:
            print(c)
            if len(freqs[r]) == 0:
                r -= 1
                print('ye')
            else:
                ans.append(freqs[r][-1])
                c += 1
                freqs[r].pop()
        return ans













class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most frequent elements
        t = len(nums)
        from collections import defaultdict
        m = defaultdict(int)

        for n in nums:
            m[n] += 1
        # group by freqs
        freqs = [[] for _ in range(t+1)]
        print(freqs)

        print(m)
        for n, freq in m.items():
            freqs[freq].append(n)

        print(freqs)
        r = t
        c = 0
        ans = []
        print('--')
        while c < k and r >= 0:
            print(c)
            if len(freqs[r]) == 0:
                r -= 1
                print('ye')
            else:
                ans.append(freqs[r][-1])
                c += 1
                freqs[r].pop()
        return ans

