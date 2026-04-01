#
# Complete the 'maximizeNonOverlappingMeetings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY meetings as parameter.
#

def maximizeNonOverlappingMeetings(meetings):
    # Write your code here
    meetings.sort(key=lambda x: x[1])
    # for item in meetings:
    print(meetings)

if __name__ == '__main__':
    meetings = [[1, 2], [1, 3], [2, 3], [3, 4]]


    result = maximizeNonOverlappingMeetings(meetings)

    print(result)