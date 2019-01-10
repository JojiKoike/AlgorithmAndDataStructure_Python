n, k = map(int, input().split())
w = [int(input()) for i in range(n)]


def check(p: int) -> int:
    i = 0
    for j in range(k):
        s = 0
        while s + w[i] <= p:
            s += w[i]
            i += 1
            if i == n:
                return n
    return i


def solve() -> int:
    left: int = 1
    right: int = 100000 * 10000
    while right - left > 1:
        mid: int = int((right + left) /2)
        v = check(mid)
        if v >= n:
            right = mid
        else:
            left = mid
    return right


if __name__ == '__main__':
    print(solve())


