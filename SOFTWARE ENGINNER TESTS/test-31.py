#
# Complete the 'findNextGreaterElementsWithDistance' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY readings as parameter.
#


def findNextGreaterElementsWithDistance(readings):

    result = []

    def next_max(array, elem):
        for item in array:
            if item > elem:
                return item
        return -1

    for i in range(len(readings)):
        right_max = next_max(readings[i:], readings[i])
        if right_max == -1:
            result.append([-1, -1])
        else:
            distance = abs(readings.index(right_max) - i)
            result.append([right_max, distance])

    return result

def findNextGreaterElementsWithDistance(readings):
    n = len(readings)
    result = [[-1, -1] for _ in range(n)]
    stack = []

    for i, value in enumerate(readings):
        while stack and readings[stack[-1]] < value:
            idx = stack.pop()
            result[idx] = [value, i - idx]
        stack.append(i)
    return result



if __name__ == '__main__':
    readings = [2, 1, 2, 4, 3]

    result = findNextGreaterElementsWithDistance(readings)

    print('\n'.join([' '.join(map(str, x)) for x in result]))