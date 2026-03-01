#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def mergeHighDefinitionIntervals(intervals):
    # Write your code here
    intervals.sort()
    i = 0
    j = 1

    while i < len(intervals) and j < len(intervals):
        while intervals[i] is None and i < len(intervals) and j < len(intervals):
            i += 1
        firstItem = intervals[i]
        second = intervals[j]

        if firstItem and second and firstItem[1] >= second[0]:
            if firstItem[1] < second[1]:
                intervals[i][1] = second[1]
            intervals[j] = None
            j += 1
        else:
            j += 1
            i += 1

    newList = []
    for item in intervals:
        if item:
            newList.append(item)
    return newList


if __name__ == '__main__':

    intervals = [[1,10], [2,3], [4,5], [6,7]]

    result = mergeHighDefinitionIntervals(intervals)

    print(result)