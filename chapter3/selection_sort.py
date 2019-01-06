def selection_sort(a, n):
    res = 0
    for i in range(0, n):
        minj = i
        for j in range(i, n):
            if a[j] < a[minj]:
                minj = j
        if i != minj:
            tmp = a[i]
            a[i] = a[minj]
            a[minj] = tmp
            res += 1
    print(a)
    print(res)


n = int(input())
a = list(map(int, input().split()))
selection_sort(a, n)
