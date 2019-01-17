from typing import List


class Card:
    def __init__(self, suit: str, value: int) -> None:
        self.suit: str = suit
        self.value: int = value


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
cards: List[Card] = []
for i in range(n):
    suit, value = input().split()
    cards.append(Card(suit, int(value)))
quick_sort(cards, 0, n - 1)
print(cards)