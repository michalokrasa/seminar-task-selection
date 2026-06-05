def reachable_numbers(n):
    visited = set()
    current = n
    
    while current not in visited:
        visited.add(current)
        current += 1
        while current % 10 == 0:
            current //= 10
    
    return len(visited)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    print(reachable_numbers(n))