def minimum_operations(n, hand, pile):
    # Find the longest prefix of pile that is already sorted
    max_sorted_prefix = 0
    current = 1
    for card in pile:
        if card == current:
            max_sorted_prefix += 1
            current += 1
        elif card != 0:
            break

    # Calculate the number of operations needed
    # We need to place all cards from current to n
    # Each card needs one operation to draw and one to play
    remaining_cards = n - max_sorted_prefix
    return remaining_cards * 2

# Read input
n = int(input().strip())
hand = list(map(int, input().strip().split()))
pile = list(map(int, input().strip().split()))

# Compute and print the result
print(minimum_operations(n, hand, pile))