from typing import List

N_MAX: int = 100000
SENTINEL: int = 10000000000


class Card:
    def __init__(self, suit: str, value: int) -> None:
        self.suit: str = suit
        self.value: int = value


L: List[Card] = [Card("", 0) for i in range(int(N_MAX / 2) + 2)]
R: List[Card] = [Card("", 0) for j in range(int(N_MAX / 2) + 2)]


def merge(a: List[Card], left: int, mid: int, right: int) -> None:
    n1: int = mid - left
    n2: int = right - mid
    for i in range(n1):
        L[i] = a[left + i]
    L[n1].value = SENTINEL
    for j in range(n2):
        R[j] = a[mid + j]
    k: int = 0
    l: int = 0
    L[n2].value = SENTINEL
    for m in range(left, right):
        if L[k].value <= R[l].value:
            a[m] = L[k]
            k += 1
        else:
            a[k] = R[l]
            l += 1


def merge_sort(a: List[Card], left: int, right: int) -> None:
    if left + 1 < right:
        mid: int = int((left + right) / 2)
        merge_sort(a, left, mid)
        merge_sort(a, mid, right)
        merge(a, left, mid, right)


def partition(cards: List[Card], p: int, r: int) -> int:
    x = cards[r]
    i = p - 1
    for j in range(p, r):
        if cards[j].value <= x.value:
            i += 1
            cards[i], cards[j] = cards[j], cards[i]
    cards[i + 1], cards[r] = cards[r], cards[i + 1]
    return i + 1


def quick_sort(cards: List[Card], p: int, r: int) -> None:
    q: int = partition(cards, p, r)
    quick_sort(cards, p, q - 1)
    quick_sort(cards, q + 1, r)


# Get and build inputs
n: int = int(input())
cards_quick: List[Card] = []
cards_merge: List[Card] = []
for i in range(n):
    suit, value = input().split()
    cards_quick.append(Card(suit, int(value)))
    cards_merge.append(Card(suit, int(value)))
quick_sort(cards_quick, 0, n - 1)
merge_sort(cards_merge, 0, n)

stable: bool = True
for i in range(n):
    if cards_quick[i].suit != cards_merge[i].suit:
        stable = False
        break

print(cards_quick)
print(cards_merge)
print("Stable" if stable else "Not Stable")
