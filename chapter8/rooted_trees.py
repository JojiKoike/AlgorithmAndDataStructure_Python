from typing import List


class Node:
    """
    Node Class
    """
    def __init__(self, parent: int, left: int, right: int):
        self.parent = parent
        self.left = left
        self.right = right


N_MAX: int = 100005
NIL: int = -1


def print_result(i: int) -> None:
    # Node Number
    print("node {0}".format(i), end=": ")
    # Parent ID
    print("parent = {0}".format(T[i].parent), end=", ")
    # Node Depth
    print("depth = {0}".format(D[i]))
    # Node Type
    node_type: str
    if T[i].parent == NIL:
        node_type = "root"
    elif T[i].left == NIL:
        node_type = "leaf"
    else:
        node_type = "internal node"
    print(node_type, end=", ")
    # Children
    c: int = T[i].left
    print("[", end="")
    while c != NIL:
        if T[c].right == NIL:
            print(c, end="")
        else:
            print(c, end=", ")
        c = T[c].right
    print("]")


def calc_depth_rec(u: int, p: int) -> None:
    D[u] = p
    if T[u].right != NIL:
        calc_depth_rec(T[u].right, p)
    elif T[u].left != NIL:
        calc_depth_rec(T[u].left, p + 1)


# Build Rooted Tree Data Structure
n: int = int(input())
T: List[Node] = [Node(NIL, NIL, NIL) for i in range(n)]
D: List[int] = [0 for i in range(n)]
v: int
d: int
left_side: int = 0
root: int = 0
for j in range(n):
    inputs: List[int] = list(map(int, input().split()))
    v = inputs[0]
    d = inputs[1]
    for k in range(d):
        c: int = inputs[k + 2]
        if k == 0:
            T[v].left = c
        else:
            T[left_side].right = c
        left_side = c
        T[c].parent = v

# Calc Root Node
for m in range(n):
    if T[m].parent == NIL:
        root = m

# Calc Each Node Depth
calc_depth_rec(root, 0)

# Print Result
for i in range(n):
    print_result(i)
