from typing import List, Any, Optional


class Node(object):
    def __init__(self, key: int, left: Any, parent: Any, right: Any):
        self.key = key
        self.left = left
        self.parent = parent
        self.right = right

root: Optional[Node] = None
NIL: Optional[Node] = None


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


def tree_minimum(x: Node) -> Node:
    while x.left != NIL:
        x = x.left
    return x


def tree_scucessor(x: Node) -> Node:
    if x.right != NIL:
        return tree_minimum(x.right)
    y: Node = x.parent
    while y != NIL and x == y.right:
        x = y
        y = y.parent
    return y


def tree_delete(z: Node) -> None:
    y: Optional[Node] = None   # Delete Target Node
    x: Optional[Node] = None   # y's children

    if z.left == NIL or z.right == NIL:
        y = z
    else:
        y = tree_scucessor(z)

    if y.left != NIL:
        x = y.left
    else:
        x = y.right

    if x != NIL:
        x.parent = y.parent

    if y.parent == NIL:
        root = x
    else:
        if y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

    if z != y:
        z.key = y.key


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
            tree_delete(find(root, int(cmd[1])))
    else:
        if cmd[0] == 'print':
            inorder(root)
            print()
            preorder(root)
            print()


