class Solution:
    def dfs(self, board, cell, word, i):
        if i == len(word):
            return True # made it to the end of the word

        # directions
        res = False
        x, y = cell[0], cell[1]
        for dx,dy in [[0,1], [0,-1], [1, 0], [-1,0]]:
            nx,ny = x+dx, y+dy
            if 0 <= nx < self.m and 0 <= ny < self.n:
                # print(nx, ny)
                if board[nx][ny] != '-1' and board[nx][ny] == word[i]:
                    l = board[nx][ny]
                    board[nx][ny] = '-1' # mark as visited
                    if i < len(word): # prune
                        if self.dfs(board, (nx, ny), word, i+1):
                            return True
                    board[nx][ny] = l # backtrack 
        
        return False



    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.m = m
        self.n = n

        # cells to start from
        cells = []
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    cells.append((r,c))
        
        for c in cells:
            # start dfs on every potential start
            l = word[0]
            board[c[0]][c[1]] = '-1'
            t = self.dfs(board, c, word, 1)
            board[c[0]][c[1]] = l
            if t:
                return True
        
        return False

