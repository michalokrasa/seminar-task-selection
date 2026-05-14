def count_flip_positions(n, sequence):
    # Check if the sequence is already regular
    def is_regular(seq):
        balance = 0
        for char in seq:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    # Calculate the balance of the sequence
    balance = 0
    for char in sequence:
        if char == '(':
            balance += 1
        else:
            balance -= 1

    # If the sequence is not balanced, no single flip can fix it
    if balance != 0:
        return 0

    # Calculate prefix balances
    prefix_balance = [0] * n
    balance = 0
    for i in range(n):
        if sequence[i] == '(':
            balance += 1
        else:
            balance -= 1
        prefix_balance[i] = balance

    # Count valid flip positions
    flip_count = 0
    if is_regular(sequence):
        return 0

    for i in range(n):
        if sequence[i] == '(':
            if prefix_balance[i] - 2 >= 0 and (i == n-1 or prefix_balance[i] - 2 + (prefix_balance[n-1] - prefix_balance[i]) == 0):
                flip_count += 1
        else:
            if prefix_balance[i] + 2 >= 0 and (i == n-1 or prefix_balance[i] + 2 + (prefix_balance[n-1] - prefix_balance[i]) == 0):
                flip_count += 1

    return flip_count

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
sequence = data[1]

# Output the result
print(count_flip_positions(n, sequence))