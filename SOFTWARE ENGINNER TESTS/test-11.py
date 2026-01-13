#
# Complete the 'countAffordablePairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER budget
#

def countAffordablePairs(prices, budget):
	i = 0
	len_ = len(prices)
	count = 0
	for i in range(len_):
		for j in range(i + 1, len_):
			print("Hi me")
			if prices[i] + prices[j] <= budget:
				count += 1

	return count

def countAffordablePairs(prices, budget):
	left = 0
	right = len(prices) - 1
	count = 0

	[1, 2, 3, 4, 5]
	while left < right:
		if prices[left] + prices[right] <= budget:
			print("left ++")
			count += (right - left) # (5 - 1) + (5 - 2) + (4 - 3) = 8
			left += 1
		else:
			print("right --")
			right -= 1

	return count

if __name__ == '__main__':
	prices = [1, 2, 3, 4, 5]
	budget = 7
	print(countAffordablePairs(prices, budget))