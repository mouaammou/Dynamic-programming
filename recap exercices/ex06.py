"""Maximum Number of Non-Overlapping Intervals
Given an array of intervals where each interval has a start and end time, return the maximum number of non-overlapping intervals."""

#
# Complete the 'maximizeNonOverlappingMeetings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY meetings as parameter.
#

def maximizeNonOverlappingMeetings(meetings):
	meetings_sorted = sorted(meetings, key=lambda x: x[1])
	count = 1

	last_end = meetings_sorted[0][1]
	for i in range(len(meetings_sorted)):
		if last_end <= meetings_sorted[i][0]:
			count += 1
			last_end = meetings_sorted[i][1]
	
	return count

if __name__ == '__main__':
	meetings = [[1, 2], [2, 3]]


	result = maximizeNonOverlappingMeetings(meetings)

	print(result)