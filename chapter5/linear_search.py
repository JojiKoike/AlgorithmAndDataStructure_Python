from typing import List

NOT_FOUND = -1


# Linear Search
def linear_search(a: List[int], n: int, key: int) -> bool:
    i: int = 0
    a[n] = key
    while a[i] != key:
        i += 1
    return i != n


n = int(input())
s = list(map(int, input().split()))
s.append(0)
q = int(input())
t = list(map(int, input().split()))

result: int = 0
for i in range(q):
    if linear_search(s, n, t[i]):
        result += 1

print("Result : {0}".format(result))