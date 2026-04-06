
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
   low = 0
   high = len(nums) - 1

   while (low <= high):
      middle = ((low + high) // 2)
      if nums[middle] == target:
         return middle
      elif target > nums[middle]:
         low = middle + 1
      else:
         high = middle - 1

   return -1


if __name__ == "__main__":

   nums = [2, 4, 6, 8, 10, 12, 14, 16]
   target = 16

   print(binarySearch(nums, target))