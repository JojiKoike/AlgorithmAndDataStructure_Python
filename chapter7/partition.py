from typing import List


def partition(a: List[int], p: int, r: int) -> int:
    x: int = a[r]
    i: int = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


N: int = int(input())
A: List[int] = list(map(int, input().split()))
q: int = partition(A, 0, N - 1)
for i in range(N):
    if i == q:
        print("[{0}]".format(A[i]), end=" ")
    else:
        print("{0}".format(A[i]), end=" ")
print()
