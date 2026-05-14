def count_picks(deck):
    from collections import deque
    
    deck = deque(deck)
    picks = 0
    sorted_deck = sorted(deck)
    
    while deck:
        picks += 1
        top_card = deck.popleft()
        if top_card == sorted_deck[0]:
            sorted_deck.pop(0)
        else:
            deck.append(top_card)
    
    return picks

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])
    deck = list(map(int, data[1:n+1]))
    print(count_picks(deck))