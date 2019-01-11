from typing import List

M: int = 1046527
NIL: int = -1

def conv_char_to_int(c: str) -> int:
    if c == 'A':
        return 1
    elif c == 'C':
        return 2
    elif c == 'G':
        return 3
    elif c == 'F':
        return 4
    else:
        return 0


def get_key(value: str) -> int:
    sum: int = 0
    p = 1
    for c in value:
        sum += p * conv_char_to_int(c)
        p *= 5
    return sum


def h1(key: int) -> int:
    return key % M


def h2(key: int) -> int:
    return 1 + key % (M -1)

H = ["" for i in range(M)]


def insert(value: str) -> int:
    key: int = get_key(value)
    i = 1
    while True:
        h = (h1(key) + i * h2(key)) % M
        if H[h] == value:
            return 1
        elif len(H[h]) == 0:
            H[h] = value
            return 0
        i += 1


def find(value: str) -> int:
    key: int = get_key(value)
    i = 1
    while True:
        h = (h1(key) + i * h2(key)) % M
        if H[h] == value:
            return 1
        elif len(H[h]) == 0:
            return 0
        i += 1


n = int(input())
for i in range(n):
    cmd, value = input().split()
    if cmd[0] == 'i':
        insert(value)
    elif cmd[0] == 'f':
        if find(value) == 1:
            print("Found")
        else:
            print("Not found")
