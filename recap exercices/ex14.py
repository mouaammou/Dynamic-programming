def findTaskPairForSlot(taskDurations, slotLength):
	seen = {}  # value → index
	for i, duration in enumerate(taskDurations):
		# print(i, duration)
		complement = slotLength - duration
		if complement in seen:
			return [seen[complement], i]
		seen[duration] = i
	return [-1, -1]



if __name__ == '__main__':
		
	taskDurations = [2, 7, 11, 15]
	slotLength = 9

	result = findTaskPairForSlot(taskDurations, slotLength)

	print('\n'.join(map(str, result)))