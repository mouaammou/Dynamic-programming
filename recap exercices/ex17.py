def canPlaceSecurityCameras(N, grid):
    N = len(grid)
    cols = set()
    diag1 = set()  # row - col  (top-left to bottom-right)
    diag2 = set()  # row + col  (top-right to bottom-left)

    def backtrack(row):
        if row == N:
            return True                          # placed all N cameras
        for col in range(N):
            if grid[row][col] == 1:              # blocked cell
                continue
            if col in cols or (row-col) in diag1 or (row+col) in diag2:
                continue                          # conflict
            # place camera
            cols.add(col)
            diag1.add(row-col)
            diag2.add(row+col)

            if backtrack(row + 1):
                return True
            # remove camera (backtrack)
            cols.remove(col); diag1.remove(row-col); diag2.remove(row+col)
        return False                             # no valid column in this row
    
    return backtrack(0)


if __name__ == '__main__':
    N = 4
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    result = canPlaceSecurityCameras(N, grid)

    print((result))