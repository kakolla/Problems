class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for i in range(len(nums))]

        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]

        # construct prefix & postfix arrs
        for i in range(len(nums)):
            if i-1 >= 0:
                prefix[i] = prefix[i-1] * nums[i]
            else:
                prefix[i] = nums[i]
        
        #postfix
        for i in range(len(nums)-1, -1, -1):
            if i+1 < len(nums):
                postfix[i] = postfix[i+1] * nums[i]
            else:
                postfix[i] = nums[i]

        print(prefix)
        print(postfix)
        #construct answer
        for k in range(len(nums)):
            prodleft = 1
            prodright = 1
            if k-1 >= 0:
                prodleft = prefix[k-1]
            if k+1 < len(nums):
                prodright = postfix[k+1]
            ans[k] = prodleft * prodright
        
        return ans