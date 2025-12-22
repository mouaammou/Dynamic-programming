def canSum(target, array):
   if (target == 0): return True
   if (target < 0): return False

   for item in array:
      result = target - item
      if (canSum(result, array) == True):
         return True
      
   return False

def canSumMemo(target, array, memo=None):
   if (memo is None): memo = {}
   if (target in memo): return memo[target]
   if (target == 0): return True
   if (target < 0): return False

   for item in array:
      result = target - item
      
      if (canSumMemo(result, array, memo) == True):
         memo[target] = True
         return True
   memo[target] = False
   return False


def canSum_buttom_up(target, array):
   array_result = [False for _ in range(target + 1)]
   array_result[0] = True
   print(array_result)
   for i in  range(target + 1):
      if (array_result[i]):
         for num in array:
            if (i + num <= target):
               array_result[i + num] = True

   return array_result[target]
          

# print(canSum_buttom_up(2, [1, 3, 4]))
print(canSum_buttom_up(1, [2, 0 ,5]))
# print(canSumMemo(1, [2, 0 ,5]))
# print(canSumMemo(7, [2, 4]))