#
# Complete the 'canPlaceSecurityCameras' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER N
#  2. 2D_INTEGER_ARRAY grid
#

# def canPlaceSecurityCameras(N, grid):
#     # Write your code here
#     pass

# if __name__ == '__main__':
#     N = 4
#     grid = [
#         [0, 0, 1, 0],
#         [0, 0, 0, 0],
#         [1, 0, 0, 1],
#         [0, 0, 0, 0]
#     ]

#     result = canPlaceSecurityCameras(N, grid)

#     print(int(result))

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    print("board initialized")
    print(board)

    def is_safe(row, col):
        # check column
        for r in range(row):
            if board[r][col] == 1:
                return False

        # check left diagonal
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 1:
                return False
            r -= 1
            c -= 1

        # check right diagonal
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == 1:
                return False
            r -= 1
            c += 1

        return True

    def backtrack(row):
        if row == n:
            solutions.append([r[:] for r in board])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1      # place queen
                backtrack(row + 1)       # go to next row
                board[row][col] = 0      # remove queen (backtrack)

    backtrack(0)
    return solutions

# call the function
solutions = solve_n_queens(4)

print("hello me")
for s in solutions:
    for row in s:
        print(row)
    print()
