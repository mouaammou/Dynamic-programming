#
# Complete the 'findPeakIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY counts as parameter.
#

def findPeakIndex(counts):
    left , right = 0, len(counts) - 1

    while left < right:
        mid = (left + right) // 2
        if  counts[mid] > counts[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':

    counts = [2, 1, 3, 5, 4]
    result = findPeakIndex(counts)

    print(result)