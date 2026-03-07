#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    total_sum = responseTimes[0]
    count = 0
    for item in range(1, len(responseTimes)):
        avg = total_sum / item
        if responseTimes[item] > avg:
            count += 1
        total_sum += responseTimes[item]
    return count

if __name__ == '__main__':

    responseTimes = [100]
    #more exmaples and the expected output
    # responseTimes = [100, 200, 300, 400, 500 ] #, expected output: 4
    # responseTimes = [100, 90, 80, 70, 60] # , expected output: 0
    responseTimes = [100, 110, 90, 120, 80] #, expected output: 2

    result = countResponseTimeRegressions(responseTimes)

    print(result)