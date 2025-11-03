from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # i: m,n, walls and guards
        # o: number of unguarded cells

        # create matrix  
        grid = [[0 for i in range(n)] for j in range(m)]

        # mark walls
        for r,c in walls:
            grid[r][c] = 2 # wall
        # for all guards, mark their reach
        for r,c in guards:
            grid[r][c] = 3 # guard
        
        # sweep left to right
        for i in range(m):
            seen = False
            for j in range(n):
                if grid[i][j] == 2:
                    seen = False
                elif grid[i][j] == 3:
                    seen = True
                elif seen:
                    grid[i][j] = -1 # this cell guarded
            # go backwards
            seen = False
            for j in range(n-1,-1,-1):
                if grid[i][j] == 2:
                    seen = False
                elif grid[i][j] == 3:
                    seen = True
                elif seen:
                    grid[i][j] = -1 # this cell guarded
        
        # sweep top to bottom
        for j in range(n):
            seen = False
            for i in range(m):
                if grid[i][j] == 2:
                    seen = False
                elif grid[i][j] == 3:
                    seen = True
                elif seen:
                    grid[i][j] = -1 # this cell guarded
            seen = False
            for i in range(m-1,-1,-1):
                if grid[i][j] == 2:
                    seen = False
                elif grid[i][j] == 3:
                    seen = True
                elif seen:
                    grid[i][j] = -1 # this cell guarded


        

        # check unguarded
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count +=1 
        return count 
