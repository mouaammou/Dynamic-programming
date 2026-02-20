# Height of Binary Search Tree
# Given the root of a binary search tree, return the height of the tree. Height is the number of nodes along the longest path from root to leaf.

# Example

# Input

# n = 7
# values = [4, 2, 6, 1, 3, 5, 7]
# leftChild = [1, 3, 5, -1, -1, -1, -1]
# rightChild = [2, 4, 6, -1, -1, -1, -1]
# Output

# 3



def getBinarySearchTreeHeight(values, leftChild, rightChild):
    def height(node):
        if node == -1:
            return 0
        left = height(leftChild[node])
        right = height(rightChild[node])
        return 1 + max(left, right)
    return height(0)
    

if __name__ == '__main__':

    n = 5
    values = [10, 5, 15, 2, 7]

    leftChild  = [-1, -1, -1, -1, -1]
    rightChild = [2, 4, -1, -1, -1]
    print(getBinarySearchTreeHeight(values, leftChild, rightChild))  