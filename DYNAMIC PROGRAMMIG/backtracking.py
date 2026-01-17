def generateAngleBracketSequences(num):
	
	opens = 0
	closes = 0
	current = ""

	result = []

	def backtracking(opens, closes, current):
		if len(current) == num * 2:
			result.append(current)
			return

		if opens < num:
			backtracking(opens + 1, closes, current + "<")
		
		if  opens > closes:
			backtracking(opens, closes + 1, current + ">")


	backtracking(opens, closes, current)
	return result

print(generateAngleBracketSequences(18))