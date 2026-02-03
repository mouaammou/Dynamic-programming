# Exercise 1: Generate All Binary Strings of Length N
# Problem

# Given an integer N, generate all binary strings of length N.

# Binary string = only '0' and '1'

def generate_binary(n):
	current = ""
	result = []


	def backtracking(current):

		if len(current) == n:
			result.append(current)
			return
		
		for bit in ['0', '1']:
			backtracking(current + bit)
	
	backtracking(current)
	return result
		
		

# def all_subsets(array): this is totally not correct
# 	current = []
# 	result = []

# 	def backtracking(current):

# 		result.append(current)
# 		if len(result) == pow(2,len(array)):
# 			# print(len(result))
# 			return 
		
# 		for i in range(len(array)):
# 			if current:
# 				_item = current[len(current) - 1]
# 				if _item >= array[i]:
# 					continue
# 			backtracking(current + [array[i]])

# 	backtracking(current)
# 	return result

def all_subsets(array):
	result = []

	def backtrack(current, start):
		result.append(current)
		for i in range(start, len(array)):
			backtrack(current + [array[i]], i + 1)

	backtrack([], 0)
	return result

if __name__ == "__main__":
	# print(generate_binary(2))
	print(all_subsets([1, 2, 3]))