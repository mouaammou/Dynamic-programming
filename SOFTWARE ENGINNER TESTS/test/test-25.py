#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

# the more optimazed version from chatgpt
def mergeHighDefinitionIntervals(intervals):
    if not intervals:
        return []

    intervals.sort()
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        print("last_end: ", last_end)
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged


# def mergeHighDefinitionIntervals(intervals):
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

    intervals = [[1,2], [2,3], [4,5], [6,7], [8,9]]

    result = mergeHighDefinitionIntervals(intervals)

    print(result)