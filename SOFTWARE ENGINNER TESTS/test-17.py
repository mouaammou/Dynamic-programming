#
# Complete the 'minTasksToCancelForNoConflict' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING digits as parameter.
#

def minTasksToCancelForNoConflict(digits):
    # Write your code here
	alphabets = "abcdefghijklmnopqrstuvwxyz"

	my_phone_keys = {}
	
	i = 2
	j = 0
	my_phone_keys['0'] = '0'
	my_phone_keys['1'] = '1'
	while i <= 9:
		if i == 7 or i == 9:
			my_phone_keys[str(i)] = alphabets[j: j + 4]
			j += 4
		else:
			my_phone_keys[str(i)] = alphabets[j: j + 3]
			j += 3
		i += 1

	#trun digits to string
	my_digits = str(digits)
	result = []

	def backtracking(index, current):

		if index == len(my_digits):
			result.append(current)
			return 
		
		digit = my_digits[index]
		for letter in my_phone_keys[digit]:
			backtracking(index + 1, current + letter)
	
	if not digits:
		return []
	backtracking(0, "")

	return result


# def generate(current):

# 	if len(current) == 3:
# 		print(current)
# 		return

# 	generate(current + "1")
# 	generate(current + "0")




if __name__ == '__main__':

	print((minTasksToCancelForNoConflict(23)))