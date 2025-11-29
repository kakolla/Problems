"""
compare to top left i-1,j-1 cell if they match
"""
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i - 1 >=0 and j-1 >=0:
                    if matrix[i-1][j-1] != matrix[i][j]: 
                        return False

        return True