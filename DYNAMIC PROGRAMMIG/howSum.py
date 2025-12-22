def howSum(target, array):
   if target == 0: return []
   if target < 0: return None


   for num in array:
      sub_num = target - num
      result = howSum(sub_num, array)
      if (result is not None):
         return result + [num]

   return None

# print(howSum(901, [2]))
# print(howSum(300, [7, 14]))

# memoization

def howSum_memo(target, array, memo=None):
   if (memo is None):
      memo = {}
   if target in memo: return memo[target]
   if target == 0: return []
   if target < 0: return None

   for num in array:
      sub_num = target - num
      result = howSum_memo(sub_num, array, memo)
      if (result is not None):
         memo[target] = result + [num]
         return memo[target]

   memo[target] = None
   return None

# print(howSum_memo(900, [1]))
# print(howSum_memo(300, [7, 14]))

# bottom up approach:

# def howSum_bottom_up (target, array):
