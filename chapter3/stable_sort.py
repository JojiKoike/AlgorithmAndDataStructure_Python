from typing import List


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


def bubble(a: List[Card], n: int) -> None:
    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if a[j - 1].value > a[j].value:
                a[j -1], a[j] = a[j], a[j - 1]


def selection(a: List[Card], n: int) -> None:
    for i in range(0, n):
        minj = i
        for j in range(i, n):
            if a[minj].value > a[j].value:
                minj = j
        a[i], a[minj] = a[minj], a[i]


def is_stable(a1: List[Card], a2: List[Card], n: int) -> bool:
    for i in range(n):
        if a1[i].suit != a2[i].suit:
            return False
    return True


def printlist(c: List[Card], n: int) -> None:
    for i in range(n):
        print("{0}{1}".format(c[i].suit, c[i].value), end=" ")
    print()


n = int(input())
a = input().split()
c1 = []
c2 = []
for i in range(n):
    card = Card(a[i][0], int(a[i][1]))
    c1.append(card)
    c2.append(card)

bubble(c1, n)
selection(c2, n)

printlist(c1, n)
print("stable")
printlist(c2, n)
print("Stable" if is_stable(c1, c2, n) else "Not Stable")




