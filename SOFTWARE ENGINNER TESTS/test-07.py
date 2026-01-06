#
# Complete the 'maximizeNonOverlappingMeetings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY meetings as parameter.
#

def maximizeNonOverlappingMeetings(meetings):
	meetings.sort(key=lambda x: x[1])
	count = 1 if len(meetings) > 0 else 0
	last_end = meetings[0][1] if len(meetings) > 0 else 0

	for i in range(1, len(meetings)):
		start, end = meetings[i]
		if start >= last_end:
			last_end = end
			count += 1

	return count
		
		

if __name__ == "__main__":
	meetings = [[1, 2], [2, 3], [3, 4], [1, 3]]
	print(maximizeNonOverlappingMeetings(meetings))