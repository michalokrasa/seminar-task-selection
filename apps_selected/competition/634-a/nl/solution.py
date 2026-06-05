def can_rearrange_statues(n, a, b):
    # Find the index of the empty pedestal in both lists
    empty_a = a.index(0)
    empty_b = b.index(0)
    
    # Rotate both lists so that the empty pedestal is at the start
    a_rotated = a[empty_a+1:] + a[:empty_a]
    b_rotated = b[empty_b+1:] + b[:empty_b]
    
    # Check if the rotated lists are equal
    if a_rotated == b_rotated:
        return "YES"
    else:
        return "NO"

import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:n+1]))
b = list(map(int, data[n+1:2*n+1]))

print(can_rearrange_statues(n, a, b))