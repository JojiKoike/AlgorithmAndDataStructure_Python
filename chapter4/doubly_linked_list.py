from typing import Any, List



class Node:
    def __init__(self, key: Any):
        self.key = key
        self.prev: Node
        self.next: Node


nil: Node = Node(None)


def init() -> None:
    nil.next = nil
    nil.prev = nil


def insert(key: int) -> None:
    node = Node(key)
    node.next = nil.next
    node.prev = nil
    nil.next.prev = node
    nil.next = node


def list_search(key: int) -> Node:
    cur: Node = nil.next
    while cur != nil and key != cur.key:
        cur = cur.next
    return cur


def delete_node(t: Node) -> None:
    if t == nil:
        return
    t.next.prev = t.prev
    t.prev.next = t.next


def delete_first() -> None:
    delete_node(nil.next)


def delete_last() -> None:
    delete_node(nil.prev)


def delete_key(key: int) -> None:
    delete_node(list_search(key))


def print_list() -> None:
    arr: List[int] = []
    cur: Node = nil.next
    arr.append(cur.key)
    while cur != nil:
        cur = cur.next
        if cur != nil:
            arr.append(cur.key)
    print(sorted(arr))

init()
n = int(input())
for i in range(n):
    cmd, key = input().split()
    if cmd[0] == 'i':
        insert(int(key))
    else:
        if len(cmd) > 6:
            if cmd[6] == 'F':
                delete_first()
            elif cmd[6] == 'L':
                delete_last()
        else:
            delete_key(int(key))

print_list()