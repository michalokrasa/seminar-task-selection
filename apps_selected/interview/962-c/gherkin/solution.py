import sys
import math

def is_perfect_square(x):
    if x < 0:
        return False
    s = int(math.isqrt(x))
    return s * s == x

def min_deletions_to_perfect_square(n):
    s = str(n)
    length = len(s)
    min_deletions = float('inf')
    
    # Generate all subsequences of the number
    for mask in range(1, 1 << length):
        subsequence = []
        for i in range(length):
            if mask & (1 << i):
                subsequence.append(s[i])
        
        if subsequence[0] == '0':  # Skip leading zero subsequences
            continue
        
        num = int(''.join(subsequence))
        if is_perfect_square(num):
            min_deletions = min(min_deletions, length - len(subsequence))
    
    return min_deletions if min_deletions != float('inf') else -1

if __name__ == "__main__":
    input = sys.stdin.read
    n = int(input().strip())
    result = min_deletions_to_perfect_square(n)
    print(result)