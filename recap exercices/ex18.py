
def getAutoSaveInterval(n):
    # Write your code here
    def fib(n, memo=None):
        if memo is None:
            memo = {}
        if n == 0:
            return 1
        if n == 1:
            return 2
        if n in memo:
            return memo[n]
        
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]
    return fib(n)

if __name__ == '__main__':
    n = 200

    result = getAutoSaveInterval(n)

    print(result)