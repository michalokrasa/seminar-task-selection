def minimize_card_sum():
    import sys
    input = sys.stdin.read
    cards = list(map(int, input().strip().split()))
    
    # Calculate the total sum of all cards
    total_sum = sum(cards)
    
    # Dictionary to count occurrences of each card number
    count = {}
    for card in cards:
        if card in count:
            count[card] += 1
        else:
            count[card] = 1
    
    # Initialize the minimum sum as the total sum (no cards discarded)
    min_sum = total_sum
    
    # Check for possible discards
    for card, cnt in count.items():
        if cnt >= 2:
            # If there are at least 2 cards of the same number, consider discarding 2
            min_sum = min(min_sum, total_sum - 2 * card)
        if cnt >= 3:
            # If there are at least 3 cards of the same number, consider discarding 3
            min_sum = min(min_sum, total_sum - 3 * card)
    
    # Output the minimum possible sum
    print(min_sum)
