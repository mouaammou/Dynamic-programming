#
# Complete the 'processCouponStackOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def processCouponStackOperations(operations):
    # Write your code here
	stack = list()
	temp_stack = list()
	return_stack = list()

	for opera in operations:
		if opera.startswith("push"):
			x = int(opera.split()[1])
			stack.append(x)
			if not temp_stack or x <= temp_stack[-1]:
				temp_stack.append(x)
			else:
				temp_stack.append(temp_stack[-1])
		elif opera == "pop":
			if stack:
				stack.pop()
				temp_stack.pop()
		elif opera == "top":
			if stack:
				return_stack.append(stack[-1])
		elif opera == "getMin":
			if temp_stack:
				return_stack.append(temp_stack[-1])

	return return_stack

			

if __name__ == '__main__':
	operations = ['push 2', 'push 0', 'push 3', 'push 0', 'getMin', 'pop', 'getMin', 'pop', 'top', 'getMin']


	print(processCouponStackOperations(operations))
