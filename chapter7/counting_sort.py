from typing import List


def counting_sort(a: List[int], k: int, n: int) -> List[int]:
    c: List[int] = [0 for i in range(k + 1)]

    # Count and Record
    for j in a:
        c[j] += 1

    # Record Count number l.e. i
    for l in range(1, k + 1):
        c[l] = c[l] + c[l - 1]

    # Create Sorted List
    b: List[int] = [0 for l in range(n)]
    for m in range(n - 1, -1, -1):
        b[c[a[m]] - 1] = a[m]
        c[a[m]] -= 1

    return b


n = int(input())
a = list(map(int, input().split()))
print(counting_sort(a, max(a), n))
