n = int(input())
r = [int(input()) for i in range(n)]

max_gain = -1000000000
min_price = r[0]
for i in range(1, n):
    max_gain = max(max_gain, r[i] - min_price)
    min_price = min(min_price, r[i])

print("Result : {0}".format(max_gain))
