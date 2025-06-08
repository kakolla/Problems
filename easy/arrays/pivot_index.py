class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0 for i in range(n)]

        sum = 0
        for i in range(n):
            prefix_sum[i] = sum
            sum += nums[i]
        
        sum = 0
        post = [0 for i in range(n)]
        for i in range(n-1, -1, -1):
            post[i] = sum
            sum += nums[i]

        print(prefix_sum)
        print(post)
        for i in range(n):
            if prefix_sum[i] == post[i]:
                return i
        
        return -1

        