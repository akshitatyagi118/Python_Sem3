# Fibonacci using Dynamic Programming
# Memoization and Tabulation

# Memoization (Top-Down)
def fib_memo(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fib_memo(n - 1, dp) + fib_memo(n - 2, dp)
    return dp[n]


# Tabulation (Bottom-Up)
def fib_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Main Program
n = int(input("Enter the value of n: "))

dp = [-1] * (n + 1)

print("Fibonacci using Memoization:", fib_memo(n, dp))
print("Fibonacci using Tabulation:", fib_tab(n))