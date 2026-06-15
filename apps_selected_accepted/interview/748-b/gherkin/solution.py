def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    s = data[0]
    t = data[1]
    
    if len(s) != len(t):
        print(-1)
        return
    
    n = len(s)
    
    # Check if both strings have the same character counts
    from collections import Counter
    if Counter(s) != Counter(t):
        print(-1)
        return
    
    # Find mismatched positions
    mismatches = []
    for i in range(n):
        if s[i] != t[i]:
            mismatches.append(i)
    
    # If there are no mismatches, no swaps are needed
    if not mismatches:
        print(0)
        return
    
    # Try to find swaps
    swaps = []
    visited = [False] * n
    
    for i in mismatches:
        if visited[i]:
            continue
        for j in mismatches:
            if i != j and not visited[j] and s[i] == t[j] and s[j] == t[i]:
                swaps.append((s[i], s[j]))
                visited[i] = True
                visited[j] = True
                break
    
    # Check if all mismatches are resolved
    if all(visited[i] for i in mismatches):
        print(len(swaps))
        for swap in swaps:
            print(swap[0], swap[1])
    else:
        print(-1)
