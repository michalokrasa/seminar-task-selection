def count_flippable_positions(n, s):
    if n % 2 != 0:
        return 0

    prefix_balance = [0] * (n + 1)
    suffix_balance = [0] * (n + 1)

    # Calculate prefix balance
    for i in range(n):
        prefix_balance[i + 1] = prefix_balance[i] + (1 if s[i] == '(' else -1)

    # Calculate suffix balance
    for i in range(n - 1, -1, -1):
        suffix_balance[i] = suffix_balance[i + 1] + (1 if s[i] == ')' else -1)

    # Check if the sequence is already regular
    if prefix_balance[n] != 0:
        return 0

    # Count valid positions
    count = 0
    for i in range(n):
        if s[i] == '(':
            # Flipping '(' to ')' means we need prefix_balance[i] - 2 >= 0
            # and suffix_balance[i + 1] + 2 >= 0
            if prefix_balance[i] - 2 >= 0 and suffix_balance[i + 1] + 2 >= 0:
                count += 1
        else:
            # Flipping ')' to '(' means we need prefix_balance[i] + 2 >= 0
            # and suffix_balance[i + 1] - 2 >= 0
            if prefix_balance[i] + 2 >= 0 and suffix_balance[i + 1] - 2 >= 0:
                count += 1

    return count

# Read input
n = int(input().strip())
s = input().strip()

# Output the result
print(count_flippable_positions(n, s))