def max_removable_substring_length(s, t):
    n, m = len(s), len(t)
    
    # Find the first occurrence of t in s
    left = 0
    for char in t:
        while s[left] != char:
            left += 1
        left += 1
    
    # Find the last occurrence of t in s
    right = n
    for char in reversed(t):
        while s[right - 1] != char:
            right -= 1
        right -= 1
    
    # Calculate the maximum removable length
    max_removable = max(right - left, n - m)
    
    return max_removable

import sys
input = sys.stdin.read
data = input().strip().split()
s = data[0]
t = data[1]
print(max_removable_substring_length(s, t))