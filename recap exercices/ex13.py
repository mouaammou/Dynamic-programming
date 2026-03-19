#
# Complete the 'debounceTimestamps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY timestamps
#  2. INTEGER K
#

def debounceTimestamps(timestamps, K):
    if not timestamps:
        return 0
    
    write = 1  # first element is already "kept" at index 0
    keep = timestamps[0]
    
    for i in range(1, len(timestamps)):
        if timestamps[i] - keep >= K:
            timestamps[write] = timestamps[i]  # ← write pointer in action
            keep = timestamps[i]
            write += 1
    print(timestamps)
    return write



if __name__ == '__main__':
	timestamps = [1, 2, 3, 8, 10]
	K = 3

	result = debounceTimestamps(timestamps, K)

	print(result)