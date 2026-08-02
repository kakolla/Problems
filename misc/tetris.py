


def tetris(grid, figure):
    h = len(grid)
    w = len(grid[0])

    # find dropping pos s.t. at least ONE full row is formed (a tetris)
    # -1 if dne

    # figure too big
    if h < 3 or w < 3:
        return -1


    # figure is 3x3 (has to be in bounds)

    # first drop it
    for col in range(w-3+1):
        # possible dropping positions
        # run the drop
        row = 1 # the row to check rn
        while row < h - 3 + 1:
            fit = True
            # check if block already in the way
            for dx in range(3):
                for dy in range(3):
                    if grid[row+dx][col+dy] == 1 and figure[dx][dy]==1:
                        fit = False
            if not fit:
                break
            row += 1
        row -= 1 # previous position is good (current row collides)

        # check the figure if it completed any rows
        for dx in range(3):
            row_filled = True
            for col_index in range(w):
                # check if any spot not filled
                # col_index is within the figure's bound and 
                # if we ever catch a 0
                if not (grid[row+dx][col_index] == 1 or (col <= col_index < col+3 and figure[dx][col_index - col] == 1)  ):
                    row_filled = False

                if row_filled:
                    return col # we should place here
    return -1


    

