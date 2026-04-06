#
# Complete the 'searchRotatedTimestamps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#


def searchRotatedTimestamps(nums, target):
    
    if not nums:
        return -1
    
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        print("d")
        if nums[left] <= nums[middle]:
            if nums[left] <= target <= nums[middle]:
                right = middle - 1
                print(left, right)
                return 
            else:
                left = middle + 1
                print("s",  left, right)
            
        else:
            print(middle, right)
            return 

if __name__ == '__main__':
    nums = [1609466400, 1609470000, 1609473600, 1609459200, 1609462800]
    target = 1609459200
    result = searchRotatedTimestamps(nums, target)
    print(result)