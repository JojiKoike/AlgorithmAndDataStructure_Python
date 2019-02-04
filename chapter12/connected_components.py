from typing import List

NIL: int = -1


def dfs(k: int, color_id: int) -> None:
    """
    DFS Solver
    :param k:
    :param color_id:
    :return:
    """
    stack: List[int] = []
    color[k] = color_id
    stack.append(k)
    while len(stack) > 0:
        p: int = stack.pop()
        for i in G[p]:
            if color[i] == NIL:
                color[i] = color_id
                stack.append(i)

# Get Inputs
# Number of Nodes and Connection Info.
n: int
m: int
n, m = map(int, input().split())
color: List[int] = [NIL for i in range(n)]
G: List[List[int]] = [[] for i in range(n)]
for i in range(m):
    s: int
    t: int
    s, t = map(int, input().split())
    G[s].append(t)
    G[t].append(s)

print(G)

# Solve
color_id: int = 0
for i in range(n):
    color_id += 1
    if color[i] == NIL:
        dfs(i, color_id)

print(color)

# Questions
q: int = int(input())
for i in range(q):
    s: int
    t: int
    s, t = map(int, input().split())
    print("Yes" if color[s] == color[t] else "No")
