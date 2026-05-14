def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n = int(data[0])
    queries = data[1:]
    
    max_width = 0
    max_height = 0
    
    results = []
    
    for query in queries:
        parts = query.split()
        if parts[0] == '+':
            x, y = int(parts[1]), int(parts[2])
            max_width = max(max_width, min(x, y))
            max_height = max(max_height, max(x, y))
        elif parts[0] == '?':
            h, w = int(parts[1]), int(parts[2])
            if (max_width <= min(h, w) and max_height <= max(h, w)):
                results.append("YES")
            else:
                results.append("NO")
    
    for result in results:
        print(result)

main()