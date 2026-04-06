#
# Complete the 'debounceTimestamps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY timestamps
#  2. INTEGER K
#

def debounceTimestamps(timestamps, K):
    # Write your code here
	index_1 = 0
	index__2 = 0
	new_array = []
	while index__2 < len(timestamps):
		# print(timestamps[index__2])
		if index__2 == 0:
			new_array.append(timestamps[index__2])
			index__2 += 1
			continue
		# print(timestamps[index__2], timestamps[index_1])
		if timestamps[index__2] - timestamps[index_1] >= K:
			new_array.append(timestamps[index__2])
			index_1 = index__2

		index__2 += 1

	return len(new_array)


if __name__ == '__main__':
	timestamps = [1, 2, 3, 8, 10]
	k = 3

	print(debounceTimestamps(timestamps, k))