
#
# Complete the 'generateAngleBracketSequences' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER n as parameter.
#

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

if __name__ == '__main__':
    n = int(input().strip())

    result = generateAngleBracketSequences(n)

    print('\n'.join(result))