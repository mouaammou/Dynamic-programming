#
# Complete the 'findTaskPairForSlot' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY taskDurations
#  2. INTEGER slotLength
#

def findTaskPairForSlot(taskDurations, slotLength):
    # Write your code here
	if not taskDurations:
		return [-1, -1]
	current = 0
	_next = current + 1
	while current < len(taskDurations) and _next < len(taskDurations):
		if taskDurations[current] + taskDurations[_next] == slotLength:
			return [current, _next]
		
		if  taskDurations[current] + taskDurations[_next] != slotLength:
			_next += 1
		
		if _next >= len(taskDurations):
			current += 1
			_next = current + 1

	return [-1, -1]

def twoSum(nums, target):
	seen = {}

	for i, num in enumerate(nums):
		need = target - num

		if need in seen:
			return [seen[need], i]

		seen[num] = i

	return [-1, -1]



if __name__ == '__main__':
	taskDurations = [7, 2, 11, 15]
	slotLength = 17

	# print(findTaskPairForSlot(taskDurations, slotLength))
	print(twoSum(taskDurations, slotLength))