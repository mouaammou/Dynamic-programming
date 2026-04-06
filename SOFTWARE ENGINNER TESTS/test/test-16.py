#
# Complete the 'isAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def isAnagram(s, t):
	# Write your code here

	if len(s) != len(t):
		return 0

	angrams_1 = {}
	angrams_2 = {}

	for str1, str2 in zip(s, t):
		if str1 in angrams_1:
			angrams_1[str1] += 1
		else:
			angrams_1[str1] = 1
		
		if str2 in angrams_2:
			angrams_2[str2] += 1
		else:
			angrams_2[str2] = 1
	
	if angrams_2 == angrams_1:
		return 1
	return 0

if __name__ == '__main__':
	s = "aab"
	t = "aba"

	print(isAnagram(s, t))