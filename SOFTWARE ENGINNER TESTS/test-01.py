# Count Elements Greater Than Previous Average
# Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.


def average(array_of_numbers):
    # print("array of numbers: ", array_of_numbers)
    len_arr = len(array_of_numbers)
    sum = 0
    for num in array_of_numbers:
        sum += num
    if len_arr == 0:
        return 0
    return int (sum / len_arr)

def countResponseTimeRegressions(responseTimes):
    count = 0
    for index in range(1, len(responseTimes)):
        # print("index array: ", responseTimes[index])
        # print("average: ", average(responseTimes[0: index]))
        if average(responseTimes[0: index]) < responseTimes[index]:
            count += 1
    return count
        

if __name__ == '__main__':
    result = countResponseTimeRegressions([100, 200, 150,300])
    print(result)
