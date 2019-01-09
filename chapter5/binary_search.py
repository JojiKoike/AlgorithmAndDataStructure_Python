from typing import List


def binary_search(a: List[int], key: int) -> bool:
    left: int = 0
    right: int = len(a)
    while left < right:
        mid: int = int((left + right) / 2)
        if a[mid] == key:
            return True
        elif a[mid] < key:
            left = mid
        else:
            right = mid
    return False


n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = sorted(list(map(int, input().split())))

result: int = 0
for i in range(q):
    if binary_search(s, t[i]):
        result += 1

print("Result: {0}".format(result))

