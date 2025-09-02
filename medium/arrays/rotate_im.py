from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # transpose matrix
        for i in range(n):
            for j in range(n):
                if j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                # i.e. i = 0, j always greater than 0
                # i = 1, j > 1
                # i =2, j > 2
                # which is a diagonal
        
        # step 2 reverse rows
        for j in range(n):
            matrix[j].reverse()