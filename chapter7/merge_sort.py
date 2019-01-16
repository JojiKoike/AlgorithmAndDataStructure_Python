from typing import List

N_MAX: int = 500000
SENTINEL: int = 10000000000


L: List[int] = [0 for i in range(int(N_MAX / 2) + 2)]
R: List[int] = [0 for j in range(int(N_MAX / 2) + 2)]
count: int = 0


def merge(a: List[int], left: int, mid: int, right: int) -> None:
    n_1: int = mid - left
    n_2: int = right - mid

    for i in range(n_1):
        L[i] = a[left + i]
    L[n_1] = SENTINEL

    for j in range(n_2):
        R[j] = a[mid + j]
    R[n_2] = SENTINEL

    k: int = 0
    l: int = 0
    for m in range(left, right):
        global count
        count += 1
        if L[k] <= R[l]:
            a[m] = L[k]
            k += 1
        else:
            a[m] = R[l]
            l += 1


def merge_sort(a: List[int], left: int, right: int) -> None:
    if left + 1 < right:
        mid: int = int((left + right) / 2)
        merge_sort(a, left, mid)
        merge_sort(a, mid, right)
        merge(a, left, mid, right)


n: int = int(input())
S: List[int] = list(map(int, input().split()))
merge_sort(S, 0, n)
print(S)
print(count)
