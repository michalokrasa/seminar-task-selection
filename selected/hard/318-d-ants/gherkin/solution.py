def simulate_ant_diffusion(n, queries):
    from collections import defaultdict, deque

    # Initialize the grid with ants at the origin
    grid = defaultdict(int)
    grid[(0, 0)] = n

    # Directions for diffusion: up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Queue to process cells with 4 or more ants
    queue = deque([(0, 0)])

    # Process the diffusion
    while queue:
        x, y = queue.popleft()
        if grid[(x, y)] >= 4:
            ants_to_diffuse = grid[(x, y)] // 4
            grid[(x, y)] -= ants_to_diffuse * 4
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                grid[(nx, ny)] += ants_to_diffuse
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
    queries = [(int(data[i * 2 + 2]), int(data[i * 2 + 3])) for i in range(t)]
    
    results = simulate_ant_diffusion(n, queries)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()