def process_queries(queries):
    max_x = 0
    max_y = 0
    results = []
    
    for query in queries:
        parts = query.split()
        if parts[0] == '+':
            x, y = int(parts[1]), int(parts[2])
            max_x = max(max_x, min(x, y))
            max_y = max(max_y, max(x, y))
        elif parts[0] == '?':
            h, w = int(parts[1]), int(parts[2])
            if (max_x <= h and max_y <= w) or (max_x <= w and max_y <= h):
                results.append("YES")
            else:
                results.append("NO")
    
    return results

# Read input
import sys
input = sys.stdin.read
data = input().strip().split('\n')
n = int(data[0])
queries = data[1:n+1]

# Process queries and print results
results = process_queries(queries)
for result in results:
    print(result)