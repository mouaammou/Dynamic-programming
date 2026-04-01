#
# Complete the 'binarySearch' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def binarySearch(nums, target):
    # Write your code here
    left = 0
    right = len(nums) - 1
    # print(middle)
    while (left <= right):
        middle = (right + left) // 2
        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return -1



if __name__ == '__main__':

    nums = [10]
    target = 10

    result = binarySearch(nums, target)

    print(result)
