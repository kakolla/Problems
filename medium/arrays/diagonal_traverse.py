
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # o: array of all elements in diag order
        # i: mxn matrix
        m = len(mat)
        n = len(mat[0])

        ans = []
        # 00 
        # 10 01
        # 20 11 02 
        # 21 12 -> all elems in a diagonal share same sum i+j

        from collections import defaultdict
        sums = defaultdict(list) # 0 : [list of elems]
        for i in range(m):
            for j in range(n):
                sums[i+j].append(mat[i][j])
        
        alt = 0 
        for s in range(m+n):
            elems = sums[s]
            if s % 2 == 0:
                ans.extend(reversed(elems))
            else:
                ans.extend(elems)
        
        return ans


        
