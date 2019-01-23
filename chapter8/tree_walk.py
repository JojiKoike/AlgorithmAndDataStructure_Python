from typing import List

NIL: int = -1


class Node:
    def __init__(self, parent: int, left: int, right: int) -> None:
        self.parent = parent
        self.left = left
        self.right = right


def preorder_walk_tree(u: int) -> None:
    if u == NIL:
        return
    print("{0}".format(u), end=" ")
    preorder_walk_tree(T[u].left)
    preorder_walk_tree(T[u].right)


def inorder_walk_tree(u: int) -> None:
    if u == NIL:
        return
    inorder_walk_tree(T[u].left)
    print("{0}".format(u), end=" ")
    inorder_walk_tree(T[u].right)


def postorder_walk_tree(u: int) -> None:
    if u == NIL:
        return
    postorder_walk_tree(T[u].left)
    postorder_walk_tree(T[u].right)
    print("{0}".format(u), end=" ")


n: int = int(input())
T: List[Node] = [Node(NIL, NIL, NIL) for i in range(n)]
for i in range(n):
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
for i in range(n):
    if T[i].parent == NIL:
        root = i

print("Preorder")
preorder_walk_tree(root)
print()
print("Inorder")
inorder_walk_tree(root)
print()
print("Postorder")
postorder_walk_tree(root)
print()