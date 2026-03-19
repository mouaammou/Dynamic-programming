def processCouponStackOperations(operations):

	stack = []
	mins_stack = []
	results = []
	
	for operation in operations:
		if "push" in operation:
			
			number = int(operation.split()[1])
			stack.append(number)
			if len(mins_stack) == 0:
				mins_stack.append(number)
			else:
				mins_stack.append(min(number, mins_stack[-1]))
		elif "pop" in operation:
			stack.pop()
			mins_stack.pop()
		elif "getMin" in operation:
			results.append(mins_stack[-1])
		elif "top" in operation:
			results.append(stack[-1])
	
	return results
		

if __name__ == '__main__':
	
	operations = ['push 2', 'push 0', 'push 3', 'push 0', 'getMin', 'pop', 'getMin', 'pop', 'top', 'getMin']

	result = processCouponStackOperations(operations)

	print('\n'.join(map(str, result)))