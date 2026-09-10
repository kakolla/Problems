






from collections import deque


class Solution:


    def bfs(self, i, j, grid):
        # mark
        m, n = len(grid), len(grid[0])

        q = deque()
        q.append((i,j))


        while q:
            x, y = q.popleft()
            grid[x][y] = "0" # visit

            for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                nx, ny = x + dx, y + dy
                if 0<= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        q.append((nx,ny))

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n  = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.bfs(i, j, grid)
                    count += 1 



        return count
                   
