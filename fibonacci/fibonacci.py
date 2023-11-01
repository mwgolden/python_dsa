
def fib_with_memoization(n, lookup=None):
    """Top-down approach"""
    lookup = {} if lookup is None else lookup
    if n in lookup:
        return lookup[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    lookup[n] = fib_with_memoization(n-1, lookup) + fib_with_memoization(n-2, lookup)
    return lookup[n]


def fib_with_tabulation(n):
    """Bottom-up approach """
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


def fib_with_tabulation_constant_space(n):
    before_prev, prev, curr = 0, 1, 1
    for i in range(2, n+1):
        curr = before_prev + prev
        before_prev = prev
        prev = curr
    return prev

