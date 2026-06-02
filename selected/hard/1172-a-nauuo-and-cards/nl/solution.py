def min_operations_to_sort_pile(n, hand, pile):
    # Check if the pile is already sorted
    if pile == list(range(1, n + 1)):
        return 0

    # Find the longest prefix of the pile that is already sorted
    longest_sorted_prefix = 0
    for i in range(n):
        if pile[i] == i + 1:
            longest_sorted_prefix += 1
        else:
            break

    # If the longest sorted prefix is k, we need at least n - k operations
    # to bring the remaining cards in order
    min_operations = n - longest_sorted_prefix

    # Check if we can do better by considering the cards in hand
    # We need to find the longest sequence of cards that can be placed
    # in order from the hand and pile combined
    position = [0] * (n + 1)
    for i in range(n):
        if pile[i] != 0:
            position[pile[i]] = i + 1

    # Calculate the minimum operations needed
    max_position = 0
    for i in range(1, n + 1):
        if position[i] > max_position:
            max_position = position[i]
        else:
            min_operations = max(min_operations, n + i - max_position)

    return min_operations

# Read input
n = int(input().strip())
hand = list(map(int, input().strip().split()))
pile = list(map(int, input().strip().split()))

# Output the result
print(min_operations_to_sort_pile(n, hand, pile))