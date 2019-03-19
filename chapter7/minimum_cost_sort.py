from typing import List

VMAX: int = 10000


def solve(a: List[int]) -> int:
    ans: int = 0
    n: int = len(a)
    s: int = min(a)
    v: List[bool] = [False for i in range(n)]
    b: List[int] = []
    for i in range(n):
        b.append(a[i])
    b.sort()
    t: List[int] = [0 for i in range(VMAX + 2)]
    for i in range(n):
        t[b[i]] = i

    for i in range(n):
        if v[i]:
            continue
        cur: int = i
        s_i: int = 0
        m: int = VMAX
        an: int = 0
        while not v[cur]:
            v[cur] = True
            an += 1
            v_i: int = a[cur]
            m = min(m, v_i)
            s_i += v_i
            cur = t[v_i]
        ans += min(s_i + (an - 2) * m, m + s_i + (an + 1) * s_i)
    return ans


a_i: List[int] = list(map(int, input().split()))
res: int = solve(a_i)
print(res)
