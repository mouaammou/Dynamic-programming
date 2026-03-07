#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def findSmallestMissingPositive(orderNumbers):
    arr_len = len(orderNumbers)
    for i in range(arr_len):
        while 1 <= orderNumbers[i] <= arr_len and orderNumbers[orderNumbers[i] - 1] != orderNumbers[i]:
            correct_order = orderNumbers[i] - 1
            orderNumbers[i], orderNumbers[correct_order] = orderNumbers[correct_order], orderNumbers[i]

    for i in range(arr_len):
        if orderNumbers[i] != i + 1:
            return i + 1
    return arr_len + 1

        

if __name__ == '__main__':

    # orderNumbers = [1, 1]
    # more exmaples and the expected output
    # orderNumbers = [1, 2, 3, 4, 5] #, expected output: 6
    # orderNumbers = [2, 3, 4, 5] #, expected output: 1
    orderNumbers = [3, 4, -1, 1] #, expected output: 2

    result = findSmallestMissingPositive(orderNumbers)

    print(result)