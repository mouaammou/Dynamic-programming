#
# Complete the 'findCombinationsByWeightIndices' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY weights
#  2. INTEGER capacity
#

def findCombinationsByWeightIndices(weights, capacity):

    result_array = []

    def backtracking(index, remaining, subarray):
        if remaining == 0:
            result_array.append(subarray[:])
        if remaining < 0:
            return 

        for i in range(index, len(weights)):
            subarray.append(i)
            backtracking(i, remaining - weights[i], subarray)
            subarray.pop()
        
    backtracking(0, capacity, [])
    return result_array



if __name__ == '__main__':
    weights = [2, 3, 6, 7]

    print(weights)
    capacity = 7

    result = findCombinationsByWeightIndices(weights, capacity)

    print('\n'.join([' '.join(map(str, x)) for x in result]))