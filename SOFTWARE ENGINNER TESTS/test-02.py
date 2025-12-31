"""
   Find the Smallest Missing Positive Integer:

      Given an unsorted array of integers, find the smallest positive integer not present in the array in O(n) time and O(1) extra space.
"""

def findSmallestMissingPositive(orderNumbers):
   orderNumbers.sort()
   missing_num = 1
   print(orderNumbers)
   for num in orderNumbers:
       if num > 0 and missing_num == num:
           missing_num += 1
   return missing_num


if __name__ == '__main__':

    orderNumbers = [1, 1]

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
