#
# Complete the 'findFirstOccurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def findFirstOccurrence(nums, target):
    # Write your code here
    # Write your code here
    left = 0
    right = len(nums) - 1
    result = -1
    # print(middle)
    while (left <= right):
        middle = (right + left) // 2
        if target == nums[middle]:
            result = middle
            right = middle - 1
        elif target > nums[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return result


if __name__ == '__main__':


    nums = [1, 3, 3, 4, 5]
    target = 3

    result = findFirstOccurrence(nums, target)

    print(result)