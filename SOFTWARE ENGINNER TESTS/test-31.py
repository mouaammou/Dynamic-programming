#
# Complete the 'findNextGreaterElementsWithDistance' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY readings as parameter.
#

def findNextGreaterElementsWithDistance(readings):
    # Write your code here

if __name__ == '__main__':
    readings = [2, 1, 2, 4, 3]

    result = findNextGreaterElementsWithDistance(readings)

    print('\n'.join([' '.join(map(str, x)) for x in result]))