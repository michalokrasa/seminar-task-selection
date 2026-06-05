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
    swaps = []
    swap_map = {}
    
    for i in range(n):
        if s[i] != t[i]:
            if (s[i], t[i]) in swap_map:
                continue
            if (t[i], s[i]) in swap_map:
                continue
            if s[i] in swap_map or t[i] in swap_map:
                print(-1)
                return
            swap_map[s[i]] = t[i]
            swap_map[t[i]] = s[i]
            swaps.append((s[i], t[i]))
    
    # Check if the swaps are valid
    for a, b in swaps:
        if swap_map.get(a) != b or swap_map.get(b) != a:
            print(-1)
            return
    
    print(len(swaps))
    for a, b in swaps:
        print(a, b)
