from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            # print("MAX: ", max_profit)
            # print("min: ", min_price)
            min_price = min(min_price, price)

        return max_profit

        # n = len(prices)
        # max_profit = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         buy_price = prices[i]
        #         profit = prices[j] - buy_price
        #         max_profit = max(max_profit, profit)
        # print(max_profit)
                

if __name__ == "__main__":
    solution = Solution()

    print(solution.maxProfit([7, 1, 5, 3, 6, 4])) 
    # print(solution.maxProfit([1, 2, 3, 4, 5]))
    # print(solution.maxProfit([7, 6, 4, 3, 1]))