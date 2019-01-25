from typing import Any, List


class Node(object):
    def __init__(self, key: int, left: Any, parent: Any, right: Any):
        self.key = key
        self.left = left
        self.parent = parent
        self.right = right


NIL: Any = None
root: Any = None


def insert(k: int):
    global NIL, root
    x: Any = root
    y: Any = NIL
    z: Node = Node(k, NIL, NIL, NIL)

    # Calc Parent Node
    while x != NIL:
        y = x
        if z.key < y.key:
            x = y.left
        else:
            x = y.right

    z.parent = y
    if y == NIL:
        root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z


def find(x: Node, k: int) -> Node:
    while x != NIL and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def inorder(u: Node) -> None:
    if u == NIL:
        return
    inorder(u.left)
    print(" {0}".format(u.key), end="")
    inorder(u.right)


def preorder(u: Node) -> None:
    if u == NIL:
        return
    print(" {0}".format(u.key), end="")
    preorder(u.left)
    preorder(u.right)


n: int = int(input())
for i in range(n):
    inputs: List[str] = input().split()
    cmd: str = inputs[0]
    if len(inputs) == 2:
        x: int = int(inputs[1])
        if cmd == 'find':
            t: Node = find(root, x)
            if t != NIL:
                print("yes")
            else:
                print("no")
        elif cmd == 'insert':
            insert(x)
    else:
        if cmd == "print":
            inorder(root)
            print()
            preorder(root)
            print()
