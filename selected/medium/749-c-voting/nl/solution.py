from collections import deque

def voting_winner(n, votes):
    d_queue = deque()
    r_queue = deque()
    
    for i, vote in enumerate(votes):
        if vote == 'D':
            d_queue.append(i)
        else:
            r_queue.append(i)
    
    while d_queue and r_queue:
        d_index = d_queue.popleft()
        r_index = r_queue.popleft()
        
        if d_index < r_index:
            d_queue.append(d_index + n)
        else:
            r_queue.append(r_index + n)
    
    return 'D' if d_queue else 'R'

# Read input
n = int(input().strip())
votes = input().strip()

# Output the winner
print(voting_winner(n, votes))