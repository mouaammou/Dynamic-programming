#
# Complete the 'findMinimumPlansForBandwidth' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY planSizes
#  2. INTEGER targetBandwidth
#

def findMinimumPlansForBandwidth(planSizes, targetBandwidth, memo=None):
    if memo == None:
        memo = {}
    if targetBandwidth in memo:
        return memo[targetBandwidth]
    if targetBandwidth == 0:
        return 0
    if targetBandwidth < 0:
        return float("inf")

    res = float("inf")
    for plan in planSizes:
        res = min(res, 1 + findMinimumPlansForBandwidth(planSizes, targetBandwidth - plan, memo))

    memo[targetBandwidth] = res
    return res


if __name__ == '__main__':
    planSizes = [1, 2, 5]
    targetBandwidth = 110

    result = findMinimumPlansForBandwidth(planSizes, targetBandwidth)

    print(result)
