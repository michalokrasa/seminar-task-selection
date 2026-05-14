def count_excessive_shocks(n, actions):
    from string import ascii_lowercase
    
    candidates = set(ascii_lowercase)
    excessive_shocks = 0
    unique_determined = False
    
    for i in range(n):
        action = actions[i]
        op, word = action[0], action[2:]
        
        if op == '.':
            if not unique_determined:
                candidates -= set(word)
        
        elif op == '!':
            if unique_determined:
                excessive_shocks += 1
            else:
                candidates &= set(word)
        
        elif op == '?':
            if not unique_determined:
                candidates.discard(word)
            if unique_determined:
                excessive_shocks += 1
        
        if len(candidates) == 1:
            unique_determined = True
    
    return excessive_shocks

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
actions = data[1:]

# Output the result
print(count_excessive_shocks(n, actions))