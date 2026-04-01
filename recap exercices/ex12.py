#
# Complete the 'generateAngleBracketSequences' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER n as parameter.
#

def generateAngleBracketSequences(num):
	result = []

	def dfs(sequence, open, close):
		if len(sequence) == num * 2:
			# print(sequence)
			result.append(sequence)
			return
		if open < num:
			dfs(sequence + "<", open + 1, close)
		if close < open:
			dfs(sequence + ">", open, close + 1)
	
	dfs("", 0, 0)
	return result
	
	

def binary_of_number(sequence ,num):
	if len(sequence) == num:
		print(sequence)
		return sequence
	binary_of_number(sequence + "1", num)
	binary_of_number(sequence + "0", num)
	

if __name__ == '__main__':
	n = int(input().strip())

	# binary_of_number("", 3)

	result = generateAngleBracketSequences(n)

	print('\n'.join(result))