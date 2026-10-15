











class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m = len(heights)
        n = len(heights[0])


        # pacific ocean 
        pac = []
        for i in range(m):
            pac.append((i, -1))
        for i in range(n):
            pac.append((-1, i))

        # atl
        at = []
        for i in range(-1, n):
            at.append((m, i))

        for i in range(0, m+1):
            at.append((i, n))


        pac_vis = set()
        at_vis = set()

        # visit all cells from pac, then at

        def visit(x, y, pacorat):

            for dx,dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                nx,ny = x+dx, y+dy
                if (x,y) in at or (x,y) in pac:
                    val = 0
                else: val = heights[x][y]
                if 0 <= nx < m and 0 <= ny < n:
                    if not pacorat and (nx,ny) in pac_vis: continue
                    if  pacorat and (nx,ny) in at_vis: continue
                    if heights[nx][ny] >= val:
                        if not pacorat: 
                            pac_vis.add((nx,ny))
                            visit(nx,ny, pacorat)
                        else:
                            at_vis.add((nx,ny))
                            visit(nx,ny, pacorat)



        for x,y in pac:
            visit(x,y,0)
        for x,y in at:
            visit(x,y,1)


        # print(pac_vis)
        # print(at_vis)
        print(at_vis.intersection(pac_vis))

        return list(at_vis.intersection(pac_vis))




