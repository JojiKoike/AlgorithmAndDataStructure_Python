from typing import List

N_MAX: int = 200000
SENTINEL: int = 10000000000


L: List[int] = [0 for i in range(int(N_MAX / 2) + 2)]
R: List[int] = [0 for j in range(int(N_MAX / 2) + 2)]


def merge(a: List[int], left: int, mid: int, right: int) -> int:
    cnt: int = 0
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
        if L[k] <= R[l]:
            a[m] = L[k]
            k += 1
        else:
            a[m] = R[l]
            l += 1
            cnt += n_1 - k
    return cnt


def merge_sort(a: List[int], left: int, right: int) -> int:
    if left + 1 < right:
        mid: int = int((left + right) / 2)
        v_1: int = merge_sort(a, left, mid)
        v_2: int = merge_sort(a, mid, right)
        v_3: int = merge(a, left, mid, right)
        return v_1 + v_2 + v_3
    else:
        return 0


n: int = int(input())
a: List[int] = list(map(int, input().split()))
print(merge_sort(a, 0, n))
