def gridTraveler(n, m):
   if (n == 0 or m == 0): return 0
   if (n == 1 and m == 1): return 1
   if ((n == 1 and m > 1) or (n > 1 and m == 1)): return 1

   return gridTraveler(n - 1, m) + gridTraveler(n, m - 1)

def gridTravelerMemo(n, m, memo={}):
   result = str(n) + "," + str(m)
   if (result in memo): 
      return memo[result]
   if (n == 0 or m == 0): return 0
   if (n == 1 and m == 1): return 1
   if ((n == 1 and m > 1) or (n > 1 and m == 1)): return 1

   memo[result] = gridTravelerMemo(n - 1, m, memo) + gridTravelerMemo(n, m - 1, memo)
   return memo[result]

def gridTraveler_buttom_up(n, m):
   array = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

   array[1][1] = 1
   for i in range(1, n + 1):
      for j in range(1, m + 1):
         if (i == 1 and j == 1): continue
         array[i][j] = array[i - 1][j] + array[i][j - 1]
   return array[n][m]
         

print(gridTraveler_buttom_up(3, 3))
print("#######")
print(gridTravelerMemo(3,3))
# print("-----------------------")
# print(gridTravelerMemo(1000,2000))