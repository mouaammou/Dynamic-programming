#
# Complete the 'countAffordablePairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER budget
#

def countAffordablePairs(prices, budget):
	
	n = len(prices)
	count = 0
	left = 0
	right = n - 1
	while left < right:
		if prices[left] + prices[right] <= budget:
			count += right - left
			left += 1
		else:
			right -= 1

	return count


if __name__ == '__main__':
	prices = [1, 2, 3, 4, 5]
	budget = 7

	result = countAffordablePairs(prices, budget)

	print(result)