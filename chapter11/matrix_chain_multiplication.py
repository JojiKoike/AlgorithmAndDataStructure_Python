from typing import List

INFTY: int = 10000000000

# Input
n: int = int(input())
p: List[int] = [0 for i in range(n + 1)]
m: List[List[int]] = [[0 if j == i else INFTY for j in range(n + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    p[i - 1], p[i] = map(int, input().split())

# Solve
for l in range(2, n + 1):
    for i in range(1, n - l + 2):
        j: int = i + l - 1
        for k in range(i, j):
            m[i][j] = min(m[i][j], m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j])

# Show Result
print("Result: {0}".format(m[1][n]))
