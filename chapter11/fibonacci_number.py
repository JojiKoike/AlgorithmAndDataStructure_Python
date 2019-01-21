from typing import List

dp: List[int]


def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        dp[n] = 1
    else:
        if dp[n] == -1:
            dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]


n: int = int(input())
dp = [-1 for i in range(n + 1)]
print("Result: {0}".format(fibonacci(n)))
print("DP Table:{0}".format(dp))
