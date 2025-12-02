class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # i: mxn grid
        # nearest gate: bfs
        m = len(rooms)
        n = len(rooms[0])
        
        # get gates
        gates = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gates.append((i,j))

        print(gates)
        from collections import deque
        q = deque()
        for gx,gy in gates:
            q.append((gx,gy, 0)) # x,y, distance
        visited = set()

        while q:
            x,y, d = q.popleft()

            for dx,dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                nx,ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited and rooms[nx][ny] != -1 and rooms[nx][ny] != 0:
                    visited.add((nx,ny))
                    q.append((nx,ny, d+1))
                    rooms[nx][ny] = d+1 # update with distance
