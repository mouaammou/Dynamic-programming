#
# Complete the 'findZeroSumTripletsInWindow' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY readings
#  2. INTEGER windowSize
#

def findZeroSumTripletsInWindow(readings, windowSize):
    end = windowSize
    result = []
    while end < len(readings):
        k = end - 1
        j = k - 1
        i = j - 1
        end += 1
        if readings[i] + readings[j] + readings[k] == 0 and (k - i + 1) <= windowSize:
            # print(readings[i], readings[j], readings[k])
            result.append([readings[i], readings[j], readings[k]])


    return result

if __name__ == '__main__':

    readings = [1, -2, 1, 0, 5]
    windowSize = 3

    result = findZeroSumTripletsInWindow(readings, windowSize)

    print('\n'.join([' '.join(map(str, x)) for x in result]))