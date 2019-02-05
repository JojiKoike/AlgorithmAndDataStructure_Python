from enum import Enum
from typing import List

INFTY: int = 10000000000


class Color(Enum):
    """
    Color definition for node visit status
    """
    WHITE: int = 1
    GRAY: int = 2
    BLACK: int = 3


def prim() -> int:
    d[0] = 0
    while True:
        minv: int = INFTY
        u: int = -1
        for i in range(n):
            if d[i] < minv and color[i] != Color.BLACK:
                u = i
                minv = d[i]
        if u == -1:
            break
        color[u] = Color.BLACK
        for v in range(n):
            if color[v] != Color.BLACK and costtable[u][v] != INFTY:
                if costtable[u][v] < d[v]:
                    d[v] = costtable[u][v]
                    p[v] = u
                    color[v] = Color.GRAY
    sum: int = 0
    for i in range(n):
        if p[i] != -1:
            sum += costtable[i][p[i]]
    return sum


n: int = int(input())
costtable: List[List[int]] = [[-1 for j in range(n)] for i in range(n)]
color: List[Color] = [Color.WHITE for k in range(n)]
d: List[int] = [INFTY for i in range(n)]
p: List[int] = [-1 for i in range(n)]
for l in range(n):
    costs: List[int] = list(map(int, input().split()))
    for m in range(n):
        costtable[l][m] = INFTY if costs[m] == -1 else costs[m]
print(prim())
