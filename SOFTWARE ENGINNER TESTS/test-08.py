#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

# def areBracketsProperlyMatched(code_snippet):
# 	brackets = []
# 	searched_str = "[({})]"
# 	opening_brackets = "{[("
# 	closed_brackets = "})]"
# 	count_opening = 0
# 	count_closed = 0

# 	for char in code_snippet:
# 		if char in searched_str:
# 			brackets.append(char)
# 			if char in opening_brackets:
# 				count_opening += 1
# 			if char in closed_brackets:
# 				count_closed += 1

# 	if count_opening != count_closed:
# 		return False
	
# 	remove_s1 = "{}"
# 	remove_s2 = '[]'
# 	remove_s3 = '()'
# 	result = ''.join(brackets)
	
# 	for i in range(count_opening):
# 		result = result.replace(remove_s1, "")
# 		result = result.replace(remove_s2, "")
# 		result = result.replace(remove_s3, "")

# 	if len(result) > 0:
# 		return False
# 	return True


def areBracketsProperlyMatched(code_snippet):
    stack = []
    opening_brackets = "{[("
    closed_brackets = "}])"
    matches = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    for char in code_snippet:
        if char in opening_brackets:
            stack.append(char)
        elif char in closed_brackets:
            if stack and stack[-1] == matches[char]:
                stack.pop() 
            else:
                return False
    
    return True if not stack else  False

if __name__ == "__main__":
	
	code_snippet = "if (a[0] > b[1]) { doSomething(); }"
	# code_snippet = 42

	# char_array = list(code_snippet)

	# print(sorted(char_array))
	print(areBracketsProperlyMatched(code_snippet)) # Should return False, but your code returns True)
	print(areBracketsProperlyMatched(")abc")) # Should return False, but your code returns True)
	print(areBracketsProperlyMatched("a(b)c)"))  # Should return False, but your code returns True