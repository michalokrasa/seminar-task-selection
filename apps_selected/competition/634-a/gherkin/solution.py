def can_rearrange_statues(n, current, desired):
    # Find the index of the empty pedestal (0) in both configurations
    current_zero_index = current.index(0)
    desired_zero_index = desired.index(0)
    
    # Rotate the current configuration to start with the empty pedestal
    rotated_current = current[current_zero_index:] + current[:current_zero_index]
    # Rotate the desired configuration to start with the empty pedestal
    rotated_desired = desired[desired_zero_index:] + desired[:desired_zero_index]
    
    # Check if the rotated configurations match
    return rotated_current == rotated_desired

import sys
input = sys.stdin.read
data = input().strip().split()

n = int(data[0])
current = list(map(int, data[1:n+1]))
desired = list(map(int, data[n+1:2*n+1]))

if can_rearrange_statues(n, current, desired):
    print("YES")
else:
    print("NO")