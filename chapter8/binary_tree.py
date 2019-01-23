from typing import List

N_MAX: int = 25
NIL: int = -1


class Node:
    def __init__(self, parent: int, left: int, right: int):
        self.parent = parent
        self.left = left
        self.right = right


def print_result(i: int) -> None:
    # Node Number
    print("node: {0}".format(i), end=": ")
    # Parent
    print("parent: {0}".format(T[i].parent), end=", ")
    # Sibling
    print("sibling = {0}".format(get_sibiling(i)), end=", ")
    # Degree
    deg :int = 0
    if T[i].left != NIL:
        deg += 1
    if T[i].right != NIL:
        deg += 1
    print("degree = {0}".format(deg), end=", ")
    # Depth
    print("depth = {0}".format(D[i]), end=", ")
    # Height
    print("height = {0}".format(H[i]), end=", ")
    # NodeType
    node_type: str
    if T[i].parent == NIL:
        node_type = "root"
    elif T[i].left == NIL and T[i].right == NIL:
        node_type = "leaf"
    else:
        node_type = "internal node"
    print(node_type)


def calc_height(u: int) -> int:
    h1: int = 0
    h2: int = 0
    if T[u].right != NIL:
        h1 = calc_height(T[u].right) + 1
    if T[u].left != NIL:
        h2 = calc_height(T[u].left) + 1
    H[u] = max(h1, h2)
    return H[u]


def calc_depth(u: int, p: int) -> None:
    if u == NIL:
        return
    D[u] = p
    calc_depth(T[u].right, p + 1)
    calc_depth(T[u].left, p + 1)


def get_sibiling(u: int) -> int:
    if T[u].parent == NIL:
        return NIL
    if T[T[u].parent].left != u and T[T[u].parent].left != NIL:
        return T[T[u].parent].left
    if T[T[u].parent].right != u and T[T[u].parent].right != NIL:
        return T[T[u].parent].right
    return NIL


n: int = int(input())
T: List[Node] = [Node(NIL, NIL, NIL) for i in range(n)]
D: List[int] = [0 for i in range(n)]
H: List[int] = [0 for i in range(n)]
for j in range(n):
    v: int
    l: int
    r: int
    v, l, r = map(int, input().split())
    T[v].left = l
    T[v].right = r
    if l != NIL:
        T[l].parent = v
    if r != NIL:
        T[r].parent = v

root: int = 0
for m in range(n):
    if T[m].parent == NIL:
        root = m

calc_depth(root, 0)
calc_height(root)

for i in range(n):
    print_result(i)
