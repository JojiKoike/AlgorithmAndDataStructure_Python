from typing import List

# Get Inputs
n: int = int(input())
m: List[List[int]] = [[0 for j in range(n + 1)] for i in range(n + 1)]
adjs: List[List[int]] = []
for i in range(n):
    adjs.append(list(map(int, input().split())))

# Build Adj. Matrix
for adj in adjs:
    for j in range(2, adj[1] + 2):
        print(adj[j])
        m[adj[0]][adj[j]] = 1

# Show Result
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(m[i][j], end=" ")
    print()


