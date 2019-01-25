from typing import List, Any


class Node(object):
    def __init__(self, key: int, left: Any, parent: Any, right: Any):
        self.key = key
        self.left = left
        self.parent = parent
        self.right = right


root: Any = None
NIL: Any = None


def insert(k: int) -> None:
    global root, NIL
    x: Node = root
    y: Node = NIL
    z: Node = Node(k, NIL, NIL, NIL)
    while x != NIL:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == NIL:
        root = z
    else:
        if z.key < y.key:
            y.left = z
        else:
            y.right = z


def find(u: Node, k: int) -> Node:
    while u != NIL and k != u.key:
        if k < u.key:
            u = u.left
        else:
            u = u.right
    return u


def delete(k: int) -> None:
    return


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


# Input, Solve
n: int = int(input())
for i in range(n):
    cmd: List[str] = input().split()
    if len(cmd) == 2:
        if cmd[0] == 'insert':
            insert(int(cmd[1]))
        elif cmd[0] == 'find':
            res: Node = find(root, int(cmd[1]))
            print("Yes" if res != NIL else "No")
        elif cmd[0] == 'delete':
            delete(int(cmd[0]))
    else:
        if cmd[0] == 'print':
            inorder(root)
            print()
            preorder(root)
            print()


