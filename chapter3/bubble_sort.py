
def bubble_sort(a, n):
    flag = 1
    res = 0
    while flag:
        flag = 0
        i = 0
        for j in range(n -1, i, -1):
            if a[j] < a[j - 1]:
                temp = a[j]
                a[j] = a[j - 1]
                a[j - 1] = temp
                res += 1
                flag = 1
        i += 1

    print(a)
    print(res)


N = int(input())
a = list(map(int, input().split()))
bubble_sort(a, N)


