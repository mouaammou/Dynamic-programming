#
# Complete the 'canPlaceSecurityCameras' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER N
#  2. 2D_INTEGER_ARRAY grid
#

def canPlaceSecurityCameras(N, grid):
    # Write your code here
    pass

if __name__ == '__main__':
    N = int(input().strip())

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = canPlaceSecurityCameras(N, grid)

    print(int(result))