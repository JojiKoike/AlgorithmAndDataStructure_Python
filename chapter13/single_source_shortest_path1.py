from enum import Enum
from typing import List

INFTY: int = 100000000


class Color(Enum):
    WHITE: int = 1
    GRAY: int = 2
    BLACK: int = 3


def dijkstra() -> None:
    d[0] = 0
    color[0] = Color.GRAY
    while True:
        minv: int = INFTY
        u: int = -1
        for i in range(n):
            if d[i] < minv and color[i] != Color.BLACK:
                u = i
                minv = d[i]
        if u == -1: break
        color[u] = Color.BLACK
        for v in range(n):
            if color[v] != Color.BLACK and m[u][v] != INFTY:
                if d[v] > d[u] + m[u][v]:
                    d[v] = d[u] + m[u][v]
                    color[v] = Color.GRAY
    for i in range(n):
        print("{0} {1}".format(i, -1 if d[i] == INFTY else d[i]))


n: int = int(input())
m: List[List[int]] = [[INFTY for j in range(n)] for i in range(n)]
d: List[int] = [INFTY for i in range(n)]
color: List[Color] = [Color.WHITE for i in range(n)]
for i in range(n):
    g: List[int] = list(map(int, input().split()))
    for j in range(1, g[1] + 1):
        m[g[0]][g[2 * j]] = g[2 * j + 1]
dijkstra()
