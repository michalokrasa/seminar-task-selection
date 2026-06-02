def min_moves_to_balance(n, matches):
    target = sum(matches) // n
    moves = 0
    imbalance = 0
    
    for match in matches:
        imbalance += match - target
        moves += abs(imbalance)
    
    return moves

# Read input
n = int(input().strip())
matches = list(map(int, input().strip().split()))

# Calculate and print the result
print(min_moves_to_balance(n, matches))