def count_reachable_numbers(n):
    visited = set()
    
    def f(x):
        while x % 10 == 0:
            x //= 10
        return x + 1
    
    while n not in visited:
        visited.add(n)
        n = f(n)
    
    return len(visited)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    print(count_reachable_numbers(n))