from typing import List

INF: int = 20000000000


def max_heapify(i: int) -> None:
    l: int = 2 * i
    r: int = 2 * i + 1
    largest: int = 0
    if l <= H and A[i] < A[l]:
        largest = l
    else:
        largest = i
    if r <= H and A[r] > A[largest]:
        largest = r
    if i != largest:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(largest)


H: int = int(input())
a: List[int] = list(map(int, input().split()))
A: List[int] = [INF for i in range(H + 1)]
for i in range(H):
    A[i + 1] = a[i]

for j in range(int(H / 2), 0, -1):
    max_heapify(j)

for k in range(1, H + 1):
    print("{0}".format(A[k]), end=" ")
print()
