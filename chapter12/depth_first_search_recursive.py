from typing import List
from enum import Enum


class Color(Enum):
    WHITE: int = 1
    GRAY: int = 2
    BLACK: int = 3


time: int = 0


def dfs_visit(u: int) -> None:
    global time
    color[u] = Color.GRAY
    time += 1
    d[u] = time
    print("time = {0}".format(time))
    for v in range(n):
        if m[u][v] and color[v] == Color.WHITE:
            dfs_visit(v)
    time += 1
    f[u] = time
    color[u] = Color.BLACK


def dfs() -> None:
    for i in range(n):
        if color[i] == Color.WHITE:
            dfs_visit(i)

    for j in range(n):
        print("{0} {1} {2}". format(j + 1, d[j], f[j]))


n: int = int(input())
adjs: List[List[int]] \
    = [list(map(int, input().split())) for i in range(n)]
d: List[int] = [0 for i in range(n)]
f: List[int] = [0 for i in range(n)]
color: List[Color] = [Color.WHITE for i in range(n)]
time = 0
m: List[List[bool]] \
    = [[False for j in range(n)] for i in range(n)]
for adj in adjs:
    for i in range(2, 2 + adj[1]):
        m[adj[0] - 1][adj[i] - 1] = True
dfs()
