from typing import List, Tuple


def shell_sort(a_i: List[int]) -> Tuple[int, List[int], int, List[int]]:
    # Build g = G_i List
    g_i: List[int] = []
    h: int = 1
    while h <= len(a_i):
        g_i.append(h)
        h = 3 * h + 1
    g_i.reverse()
    # Shell Sort
    cnt: int = 0
    for g in g_i:
        for i in range(g, len(a_i)):
            v: int = a_i[i]
            j = i - g
            while j >= 0 and a_i[j] > v:
                a_i[j + g] = a_i[j]
                print(j + g)
                j -= g
                cnt += 1
            print(j + g)
            a_i[j + g] = v

    # Return Value
    return len(g_i), g_i, cnt, a_i


a_inputs: List[int] = list(map(int, input().split()))
m: int
g: List[int]
cnt: int
a: List[int]
m, g, cnt, a = shell_sort(a_inputs)
print(m)
print(g)
print(cnt)
print(a)
