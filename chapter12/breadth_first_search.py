from typing import List, Deque
from collections import deque

INF: int = 100000000000


def bfs(s: int) -> None:
    queue.append(s)
    dists[s] = 0
    while len(queue) > 0:
       q: int = queue.popleft()
       for u in range(n):
           if not m[q][u]: continue
           if dists[u] != INF: continue
           dists[u] = dists[q] + 1
           queue.append(u)

    for i in range(n):
        print("{0} {1}".format(i + 1, dists[i]))


# Get Num. of Nodes
n: int = int(input())
# Build Adjs. Matrix
adjs: List[List[int]] = [list(map(int, input().split())) for i in range(n)]
m: List[List[bool]] = [[False for j in range(n)] for i in range(n)]
for adj in adjs:
    for k in range(2, 2 + adj[1]):
        m[adj[0] - 1][adj[k] - 1] = True
# Init. Distance List
dists: List[int] = [INF for i in range(n)]
# Init. queue
queue: Deque[int] = deque()
# Solve bfs
bfs(0)
