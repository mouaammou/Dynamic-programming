


def mergeHighDefinitionIntervals(intervals):
    if not intervals:
        return []
    
    intervals.sort()
    merged = [intervals[0]]

    for item in intervals[1:]:
        last = merged[-1]
        if last[1] >= item[0]:
            last[1] = max(last[1], item[1])
        else:
            merged.append(item)
   
    return merged

if __name__ == '__main__':

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))