def finbonacci(n):
   # base cases
   if (n == 0):
      return 0
   if (n == 1 or n == 2):
      return 1
   # recursion call
   return finbonacci(n - 1) + finbonacci(n - 2)

# print(finbonac
# time complexity is : O(2^n)   .  space is O(n)
print("#########################################")
# optimization using memoization 
def finbonacciMemo(n, memo={}):
   # base cases
   if (n in memo):
      return memo[n]
   if (n == 0):
      return 0
   if (n == 1 or n == 2):
      return 1
   # recursion call
   memo[n] = finbonacciMemo(n - 1, memo) + finbonacciMemo(n - 2, memo)
   return memo[n]


# solving the problem of recursion: RecursionError: maximum recursion depth exceeded
# using bottom-up approach or tabulation

def fib_bottom_up(n):
   array = [0]*(n + 1)
   array[0] = 1
   array[1] = 1
   for i in range(2, n + 1):
      array[i] = array[i - 1] + array[i - 2]
   
   return array[n]


# print(finbonacciMemo(5))
# print(finbonacciMemo(10))
# print(finbonacciMemo(20))
print(fib_bottom_up(10000))
