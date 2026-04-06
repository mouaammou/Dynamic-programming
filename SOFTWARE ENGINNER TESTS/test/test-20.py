
def countInstallationSequences(n):
    # Write your code here
    memo = {}
    def fibonacci(n, memo):
        if n == 0 or n == 1:
            return 1
        
        if n in memo:
            return memo[n]
        
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]
    
    return fibonacci(n, memo)