"""
   Find the Smallest Missing Positive Integer:

      Given an unsorted array of integers, find the smallest positive integer not present in the array in O(n) time and O(1) extra space.
"""

# def findSmallestMissingPositive(orderNumbers):
#     len_arr = len(orderNumbers)
#     # get rid of non wanted numbers
#     for i in range(len_arr):
#         if orderNumbers[i] > len_arr or orderNumbers[i] <= 0:
#             orderNumbers[i] = len_arr + 1

# 	# mark presence
# 	# idx: 0, 1, 2, 3, 4
# 	# num: 1, 2, 3, 4, 5
#     for i in range(len_arr):
#         val = abs(orderNumbers[i])
#         if 1 <= val <= len_arr:
#             index = val - 1
#             if orderNumbers[index] > 0:
#                 orderNumbers[index] = -orderNumbers[index]

#     for i in range(len_arr):
#         if orderNumbers[i] > 0:
#             return i + 1
#     return len_arr + 1

def findSmallestMissingPositive(orderNumbers):
    n = len(orderNumbers)
    i = 0
    while i < n:
        # Only swap if orderNumbers[i] is in [1, n] and not already in the right place
        correct_idx = orderNumbers[i] - 1
        print("correct_Index: ", correct_idx)
        print("index: ", i)
        if 1 <= orderNumbers[i] <= n and orderNumbers[i] != orderNumbers[correct_idx]:
            orderNumbers[i], orderNumbers[correct_idx] = orderNumbers[correct_idx], orderNumbers[i]
        else:
            i += 1
    print("after swapping: ", orderNumbers)

    # After sorting, the first place where orderNumbers[i] != i+1 is the answer
    for i in range(n):
        if orderNumbers[i] != i + 1:
            return i + 1
    return n + 1


if __name__ == '__main__':

    orderNumbers = [1, 0, -2, 2, 3]

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
