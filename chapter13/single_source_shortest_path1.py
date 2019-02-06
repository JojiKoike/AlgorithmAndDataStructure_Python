from typing import List

INFTY: int = 100000000


def dijkstra(i: int) -> int:
    return i


n: int = int(input())
m: List[List[int]] = [[INFTY for j in range(n)] for i in range(n)]
for i in range(n):
    g: List[int] = list(map(int, input().split()))
    for j in range(1, g[1] + 1):
        m[g[0]][g[2 * j]] = g[2 * j + 1]

print(m)

for i in range(n):
    print("{0} {1}".format(i, dijkstra(i)))
