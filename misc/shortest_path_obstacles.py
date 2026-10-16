







"""
basically a bfs (guaranteed shortest path)
but if we encounter an obstacle, subtract 1 from k to be 
allowed to pass through.

if no more left, it just gets exhausted.

the states (x,y, k left over) are tracked in visited set



"""


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:

        m = len(grid)
        n = len(grid[0])

        x,y = 0, 0

        

        from collections import deque
        q = deque() # (x,y, k left, steps )


        
        visited = set()


        def bfs():
            # pop

            while q:
                x,y, l, s = q.popleft()
                if x == m-1 and y == n-1:
                    print(k)
                    return s #return steps
                
                for dx,dy in [[0,1], [0,-1], [1,0], [-1, 0]]:
                    nx,ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx,ny,l):
                        if grid[nx][ny] and l-1 >= 0 and (nx,ny,l-1) not in visited:
                            q.append((nx,ny, l-1, s+1))
                            visited.add((nx, ny, l-1))
                        elif not grid[nx][ny]and l >= 0 and (nx,ny,l) not in visited:
                            q.append((nx,ny, l, s+1))
                            visited.add((nx, ny, l))
            return -1





                # visit neis, -1 to surpass an obstacle
                # if no more, pop that



        # add to queue
        q.append((x,y,k if not grid[x][y] else k-1, 0))
        return bfs()




