from typing import List

N_MAX: int = 1000


def lcs(x: str, y: str) -> int:
    dp: List[List[int]] = [[-1 for j in range(N_MAX + 1)] for i in range(N_MAX + 1)]
    maxl: int = 0
    m = len(x)
    n = len(y)
    for i in range(m + 1):
        dp[i][0] = 0
    for j in range(n + 1):
        dp[0][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            maxl = max(maxl, dp[i][j])
    return maxl


n: int = int(input())
for i in range(n):
    x: str = input()
    y: str = input()
    print(lcs(x, y))
