#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

def areBracketsProperlyMatched(code_snippet):
	stack = []
	opening_brackets = "([{"
	close_brackets = ")]}"
	matching = {')': '(', ']': '[', '}': '{'}


	for i in code_snippet:
		if i in opening_brackets:
			stack.append(i)
		elif i in close_brackets:
			if not stack or stack[-1] != matching[i]:
				return False
			stack.pop()
	# print(stack)
	return len(stack) == 0
if __name__ == '__main__':

	code_snippet = "()"

	result = areBracketsProperlyMatched(code_snippet)

	print((result))