







import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = nums[:k]
        heapq.heapify((pq))
        print(pq)

        for i in range(k, len(nums)):
            heapq.heappush(pq, nums[i])
            heapq.heappop(pq)

        print(pq)
        return pq[0]






       




        








import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = nums[:k]
        heapq.heapify((pq))
        print(pq)

        for i in range(k, len(nums)):
            heapq.heappush(pq, nums[i])
            heapq.heappop(pq)

        print(pq)
        return pq[0]






       




        
