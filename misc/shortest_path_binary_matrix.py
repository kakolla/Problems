













class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # return length of the hsortest clear path in the matrix
        x,y = 0,0
        from collections import deque



        q = deque()
        visited = set()

        if grid[0][0] == 1: return -1

        def bfs():

            while q:

                x,y, cost = q.popleft()

                if x == n-1 and y == n-1:
                    return cost
                
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0: continue
                        nx = dx + x
                        ny = dy + y
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx,ny) not in visited:
                            q.append((nx ,ny, cost+1))
                            visited.add((nx,ny))
            return -1






        q.append((x,y, 1))
        return bfs()
       
