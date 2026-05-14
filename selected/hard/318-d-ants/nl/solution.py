from collections import defaultdict, deque

def simulate_ants(n, queries):
    # Initialize the grid with the starting point
    grid = defaultdict(int)
    grid[(0, 0)] = n
    
    # Queue to process cells with 4 or more ants
    queue = deque()
    if n >= 4:
        queue.append((0, 0))
    
    # Directions for diffusion
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # Process the grid
    while queue:
        x, y = queue.popleft()
        ants = grid[(x, y)]
        
        if ants >= 4:
            # Calculate how many ants to move
            move_ants = ants // 4
            grid[(x, y)] -= move_ants * 4
            
            # Distribute ants to neighboring cells
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                grid[(nx, ny)] += move_ants
                # If a neighboring cell reaches 4 or more ants, add it to the queue
                if grid[(nx, ny)] >= 4 and (nx, ny) not in queue:
                    queue.append((nx, ny))
    
    # Answer the queries
    results = []
    for x, y in queries:
        results.append(grid[(x, y)])
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    t = int(data[1])
    queries = []
    
    index = 2
    for _ in range(t):
        x = int(data[index])
        y = int(data[index + 1])
        queries.append((x, y))
        index += 2
    
    results = simulate_ants(n, queries)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()