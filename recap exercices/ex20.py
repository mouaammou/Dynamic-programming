#
# Complete the 'getBinarySearchTreeHeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY leftChild
#  3. INTEGER_ARRAY rightChild
#

def getBinarySearchTreeHeight(values, leftChild, rightChild):
    
    if not values:
        return 0

    def dfs(node):
        if node == -1:
            return 0
        left_side = dfs(leftChild[node])
        right_side = dfs(rightChild[node])
        return 1 + max(left_side, right_side)

    return dfs(0)

if __name__ == '__main__':

    n = 7
    values = [4, 2, 6, 1, 3, 5, 7]
    leftChild = [1, 3, 5, -1, -1, -1, -1]
    rightChild = [2, 4, 6, -1, -1, -1, -1]

    result = getBinarySearchTreeHeight(values, leftChild, rightChild)

    print(result)