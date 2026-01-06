# Complete the 'findFirstOccurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def findFirstOccurrence(nums, target):
   # Write your code here
   low = 0
   high = len(nums) - 1
   occurence_index = -1

   while (low <= high):
      middle = (low + high) // 2
      if nums[middle] == target:
         occurence_index = middle
         high = middle - 1
      elif target > nums[middle]:
         low = middle + 1
      else:
         high = middle - 1

   return occurence_index

if __name__ == "__main__":

   nums = [1, 2, 3, 3, 3, 3, 3, 3, 4, 5]
   target = 3
   print(findFirstOccurrence(nums, target))