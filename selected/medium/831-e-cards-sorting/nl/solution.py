from collections import deque

def card_sorting(n, cards):
    card_count = {}
    for card in cards:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1

    sorted_unique_cards = sorted(card_count.keys())
    deck = deque(cards)
    total_picks = 0

    for min_card in sorted_unique_cards:
        while card_count[min_card] > 0:
            total_picks += 1
            top_card = deck.popleft()
            if top_card == min_card:
                card_count[min_card] -= 1
            else:
                deck.append(top_card)

    return total_picks

# Read input
n = int(input().strip())
cards = list(map(int, input().strip().split()))

# Output the result
print(card_sorting(n, cards))