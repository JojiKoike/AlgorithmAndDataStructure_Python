from typing import List, Any

class Node:
    def __init__(self, key: int, left: Any, parent: Any, right: Any):
        self.key = key
        self.left = left
        self.parent = parent
        self.right = right

root: Any = None
NIL: Any = None

def insert(k: int) -> None:
    global root, NIL
    y: Node = NIL   # For Parent
    x: Node = root  # For Next Node
    z: Node = Node(k, NIL, NIL, NIL)

    # Calc Parent Node
    while x != NIL:
        y = x
        if z.key < y.key:
            x = x.left
        else:
            x = x.right

    z.parent = y
    # Calc which side new node inserted into
    if y == NIL:
        root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z


def inorder(u: Node) -> None:
    if u == NIL:
        return
    inorder(u.left)
    print(" {0}".format(u.key), end="")
    inorder(u.right)


def preorder(u: Node) -> Node:
    if u == NIL:
        return
    print(" {0}".format(u.key), end="")
    preorder(u.left)
    preorder(u.right)

n: int = int(input())
for i in range(n):
    inputs: List[str] = input().split(" ")
    if len(inputs) == 2:
        if inputs[0] == 'insert':
            insert(int(inputs[1]))
    elif inputs[0] == "print":
        inorder(root)
        print()
        preorder(root)
        print()
