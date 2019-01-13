from typing import List

n: int = int(input())
a: List[int] = list(map(int, input().split()))


def find_maximum(a: List[int], l: int, r: int) -> int:
    mid: int = int((l + r) / 2)
    if l == r - 1:
        return a[l]
    else:
        u = find_maximum(a, l, mid)
        v = find_maximum(a, mid, r)
        x = max(u, v)
    return x


print(find_maximum(a, a[0], a[n - 1]))