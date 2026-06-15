def is_valid_obfuscation(s):
    # Check if the string can be a result of Kostya's obfuscation
    # The string should have characters in non-decreasing order of their first appearance
    last_seen = {}
    for i, char in enumerate(s):
        if char in last_seen:
            if i - last_seen[char] > 1:
                return "NO"
        last_seen[char] = i
    return "YES"

import sys
input = sys.stdin.read
s = input().strip()
print(is_valid_obfuscation(s))