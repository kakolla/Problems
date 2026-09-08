






class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        l, r = 0, len(numbers) - 1  

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l, r]
            elif s > target:
                r -= 1
            else:
                l +=1




        
