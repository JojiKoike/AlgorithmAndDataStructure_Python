from typing import List

INF: int = 20000000000
MAX: int = 2000000

H: int = 0
A: List[int] = [-INF for i in range(MAX + 1)]


def increase_key(i: int, key: int) -> None:
    if key < A[i]:
        return
    A[i] = key
    while i > 1 and A[int(i / 2)] < A[i]:
        A[i], A[int(i / 2)] = A[int(i / 2)], A[i]
        i = int(i / 2)


def insert(key: int) -> None:
    global H
    H += 1
    A[H] = -INF
    increase_key(H, key)


def max_heapify(i: int) -> None:
    l: int = 2 * i
    r: int = 2 * i + 1
    largest: int = 0
    if l <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= H and A[r] > A[largest]:
        largest = r
    if i != largest:
        A[i], A[largest] = A[i], A[largest]
        max_heapify(largest)


def extract() -> int:
    global H
    if H < 1:
        return
    maxv: int = A[1]
    A[1] = A[H]
    H -= 1
    max_heapify(1)
    return maxv

while True:
    cmd: List[str] = input().split()
    if cmd[0] == 'end':
        break
    elif cmd[0] == 'insert':
        insert(int(cmd[1]))
    else:
        print(extract())
