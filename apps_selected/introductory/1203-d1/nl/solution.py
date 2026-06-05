def is_subsequence(s, t):
    it = iter(s)
    return all(c in it for c in t)

def max_removable_substring_length(s, t):
    n = len(s)
    left, right = 0, n - len(t)
    
    while left < right:
        mid = (left + right + 1) // 2
        found = False
        for i in range(n - mid + 1):
            if is_subsequence(s[:i] + s[i+mid:], t):
                found = True
                break
        if found:
            left = mid
        else:
            right = mid - 1
    
    return left

import sys
input = sys.stdin.read
s, t = input().strip().split()
print(max_removable_substring_length(s, t))