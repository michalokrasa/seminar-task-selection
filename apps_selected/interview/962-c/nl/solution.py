def is_perfect_square(x):
    root = int(x**0.5)
    return root * root == x

def min_deletions_to_perfect_square(n):
    s = str(n)
    length = len(s)
    min_deletions = float('inf')
    
    # Iterate over all subsets of the digits
    for mask in range(1, 1 << length):
        candidate = []
        for i in range(length):
            if mask & (1 << i):
                candidate.append(s[i])
        
        if candidate[0] == '0':
            continue
        
        num = int(''.join(candidate))
        
        if is_perfect_square(num):
            min_deletions = min(min_deletions, length - len(candidate))
    
    return min_deletions if min_deletions != float('inf') else -1

import sys
input = sys.stdin.read
n = int(input().strip())
print(min_deletions_to_perfect_square(n))