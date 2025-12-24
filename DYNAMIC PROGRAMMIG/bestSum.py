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

print(bestSum(2, [1, 2]))
print(bestSum(50, [2, 1, 5, 25]))
print(bestSum(100, [2, 1, 5, 25]))