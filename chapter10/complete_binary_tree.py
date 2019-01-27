from typing import List

MAX: int = 100000
INF: int = 20000000000


def parent(i: int) -> int:
    return int(i / 2)


def left(i: int) -> int:
    return i * 2


def right(i: int) -> int:
    return i * 2 + 1


H: int = int(input())
a: List[int] = list(map(int, input().split()))
A: List[int] = [INF for i in range(H + 1)]
for i in range(H):
    A[i + 1] = a[i]

for i in range(1, H + 1):
    print("node {0}: key = {1}, ".format(i, A[i]), end="")
    if parent(i) >= 1:
        print("parent key = {0}, ".format(A[parent(i)]), end="")
    if left(i) <= H:
        print("left key = {0}, ".format(A[left(i)]), end="")
    if right(i) <= H:
        print("right key = {0},".format(A[right(i)]), end="")
    print()
