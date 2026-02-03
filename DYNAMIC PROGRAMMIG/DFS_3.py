
def path_finding(grid):

    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return False
        
        if visited[r][c] or grid[r][c] == 1:
            return False
        
        if grid[r][c] == 'E':
            return True
        
        visited[r][c] = True

        return (
            dfs(r + 1, c) or
            dfs(r - 1, c) or
            dfs(r, c + 1) or
            dfs(r, c - 1)
        )
    
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                return (dfs(r, c))
    

        




if __name__ == "__main__":
    
    grid = [
        ["S", 0, 1],
        [1,   0, 1],
        [0,   0, "E"]
    ]

    print(path_finding(grid))