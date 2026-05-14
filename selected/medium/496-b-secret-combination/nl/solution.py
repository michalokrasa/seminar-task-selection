def smallest_combination(n, digits):
    def add_and_rotate(digits, add_amount):
        # Add the add_amount to each digit and wrap around
        new_digits = [(int(d) + add_amount) % 10 for d in digits]
        # Convert back to string
        new_digits_str = ''.join(map(str, new_digits))
        # Find the smallest rotation
        smallest_rotation = new_digits_str
        for i in range(1, n):
            rotated = new_digits_str[i:] + new_digits_str[:i]
            if rotated < smallest_rotation:
                smallest_rotation = rotated
        return smallest_rotation

    smallest = digits
    for add_amount in range(10):
        candidate = add_and_rotate(digits, add_amount)
        if candidate < smallest:
            smallest = candidate
    return smallest

# Read input
n = int(input().strip())
digits = input().strip()

# Output the smallest combination
print(smallest_combination(n, digits))