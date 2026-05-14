def find_unique_substrings(phone_numbers):
    from collections import defaultdict

    n = len(phone_numbers)
    substrings = defaultdict(list)

    # Collect all possible substrings for each phone number
    for index, number in enumerate(phone_numbers):
        for length in range(1, 10):  # Substring lengths from 1 to 9
            for start in range(10 - length):  # Start positions for each length
                substr = number[start:start + length]
                substrings[substr].append(index)

    # Find the shortest unique substring for each phone number
    result = [''] * n
    for substr, indices in substrings.items():
        if len(indices) == 1:  # Unique substring
            index = indices[0]
            if result[index] == '' or len(substr) < len(result[index]):
                result[index] = substr

    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
phone_numbers = data[1:n+1]

# Find and print the shortest unique substrings
unique_substrings = find_unique_substrings(phone_numbers)
for substring in unique_substrings:
    print(substring)