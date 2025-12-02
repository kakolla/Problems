class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # i: matrix nxn
        # o: k'th smallest element (not distinct)
        n = len(matrix)
        # 1 3 8
        # 3 4 9
        # 1 3 9 -> look at right and bottom as those will be greater
        #       -> pq will keep mins at top

        import heapq
        pq = []
        visited = set()
        pq.append((matrix[0][0], 0, 0)) # val, row, col
        min_val = -1
        for i in range(k):
            min_val, x, y = heapq.heappop(pq)
            if x+1 < n and (x+1,y) not in visited:
                heapq.heappush(pq, (matrix[x+1][y], x+1, y))
                visited.add((x+1, y))
            if y+1 < n and (x,y+1) not in visited:
                heapq.heappush(pq, (matrix[x][y+1],x,y+1))
                visited.add((x,y+1))

        return min_val