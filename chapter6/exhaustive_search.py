from typing import List

n: int = int(input())
a: List[int] = list(map(int, input().split()))
q: int = int(input())
m: List[int] = list(map(int, input().split()))


def solve(i: int, m: int) -> bool:
    if m == 0:
        return True
    elif i >= n:
        return False
    res: bool = solve(i + 1, m) or solve(i + 1, m - a[i])
    return res


for i in range(q):
    print("yes" if solve(0, m[i]) else "no")

