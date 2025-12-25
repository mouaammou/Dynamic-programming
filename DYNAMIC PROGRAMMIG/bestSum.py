def bestSum(target, array):
   if target == 0:
      return []
   if target < 0:
      return None

   smallest_comb = None
   for num in array:
      reminder = target - num
      result = bestSum(reminder, array)
      if result is not None:
         combination = result + [num]
         if (smallest_comb is None or len(combination) < len(smallest_comb)):
            smallest_comb = combination

   return smallest_comb

# print(bestSum(2, [1, 2]))
# print(bestSum(50, [2, 1, 5, 25]))
# print(bestSum(100, [2, 1, 5, 25]))

"""
   **** BEST SOME USING MEMOIZATION ****
"""

def bestsum_memoization(target, array, memo=None):
   if memo is None: 
      memo = {}
   if target in memo:
      return memo[target]
   if target == 0:
      return []
   if target < 0: 
      return None
   
   smallest_combination = None
   for num in array:
      reminder = target - num
      result = bestsum_memoization(reminder, array, memo)
      if result is not None:
         combination = result + [num]
         if smallest_combination is None or len(combination) < len(smallest_combination):
            smallest_combination = combination

   memo[target] = smallest_combination
   return smallest_combination

print("memoization -->")
print(bestsum_memoization(2, [1, 2]))
print(bestsum_memoization(50, [2, 1, 5, 25]))
print(bestsum_memoization(100, [2, 1, 5, 25]))
print(bestsum_memoization(1000, [2, 1, 5, 25]))


"""
   **** best_sum using tabulation ****
"""

def best_sum_tabulation(target, array):
   table = [None for _ in range(target + 1)]
   table[0] = []
   for i in range(target + 1):
      if table[i] is not None:
         for num in array:
            if i + num <= target:
               combination = table[i] + [num]
               if table[i + num] is None or (len(table[i + num]) > len(combination)):
                  table[i + num] = combination
               
   
   return table[target]

print("tabulation -->")
print(best_sum_tabulation(2, [1, 2]))
print(best_sum_tabulation(50, [2, 1, 5, 25]))
print(best_sum_tabulation(100, [2, 1, 5, 25]))
print(best_sum_tabulation(100000, [2, 1, 5, 25]))
