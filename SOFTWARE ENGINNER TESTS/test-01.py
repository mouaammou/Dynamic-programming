# Count Elements Greater Than Previous Average
# Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.


def countResponseTimeRegressions(responseTimes):
    count = 0
    sum = responseTimes[0]
    for index in range(1, len(responseTimes)):
        avr = sum / index
        if responseTimes[index] > avr:
            count += 1
        sum += responseTimes[index]
    return count

if __name__ == '__main__':
    result = countResponseTimeRegressions(list(range(1, 100_000_000)))
    print(result)
