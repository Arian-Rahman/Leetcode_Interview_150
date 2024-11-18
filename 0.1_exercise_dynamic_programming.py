




"""
fibonaci
"""

def fib_topDown_(n, memo=None):
    if memo is None:
        memo = {}  # Initialize the memo dictionary if it doesn't exist
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


def fib_bottomUp (n):
    if n<-1:
        return n
    
    dp = [0] * (n+1)
    dp[0],dp[1] = 0,1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]


def main():
    print("Fibonacci number calculator")
    n = int(input("Enter a number to calculate the nth Fibonacci number: "))
    #result = fib(n)
    result = fib_bottomUp(n)
    print(f"The {n}th Fibonacci number is: {result}")

if __name__ == "__main__":
    main()
