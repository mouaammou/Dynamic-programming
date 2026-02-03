#    EXERCISE 2: Count islands in a grid (classic DFS)

# This is the most important DFS exercise ever.

#  Problem

# Given a grid of 0 (water) and 1 (land), count how many islands there are.
# An island = connected 1s (up, down, left, right).

grid = [
    [1, 1, 0],
    [0, 1, 0],
    [1, 0, 1]
]

rows = len(grid)
cols = len(grid[0])

def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if grid[r][c] == 0:
        return

    grid[r][c] = 0  # mark as visited

    dfs(r + 1, c)  # down
    dfs(r - 1, c)  # up
    dfs(r, c + 1)  # right
    dfs(r, c - 1)  # left


count = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 1:
            dfs(r, c)
            count += 1

print(count)