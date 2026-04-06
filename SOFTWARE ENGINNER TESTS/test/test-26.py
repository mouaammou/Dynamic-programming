#
# Complete the 'findLongestArithmeticProgression' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findLongestArithmeticProgression(arr, k):
    # we need to to sort the array and remove duplicats
    arr = sorted(set(arr))
    max_len = 0
    dp = {}

    for x in arr:
        if x - k in dp:
            dp[x] = dp[x - k] + 1
        else:
            dp[x] = 1
        max_len = max(max_len, dp[x])

    return max_len

if __name__ == '__main__':

    arr = [8, 1, -1, 0, 3, 6, 2, 4, 5, 7, 9]
    k = 2

    result = findLongestArithmeticProgression(arr, k)

    print(result)