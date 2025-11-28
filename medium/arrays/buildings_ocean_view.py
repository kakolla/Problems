class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        # o: indices of buildings that are strictly taller than all on the right
        ans = []
        tallest = 0
        for i in range (n-1, -1, -1):
            if heights[i] > tallest:
                ans.append(i)
            tallest = max(tallest, heights[i])
        
        return ans[::-1]
