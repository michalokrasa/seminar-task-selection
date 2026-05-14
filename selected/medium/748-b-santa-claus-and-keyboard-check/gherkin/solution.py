def find_swaps(s, t):
    if s == t:
        print(0)
        return

    if len(s) != len(t):
        print(-1)
        return

    swap_map = {}
    reverse_map = {}
    swaps = []

    for i in range(len(s)):
        if s[i] != t[i]:
            if s[i] in swap_map and swap_map[s[i]] != t[i]:
                print(-1)
                return
            if t[i] in reverse_map and reverse_map[t[i]] != s[i]:
                print(-1)
                return
            swap_map[s[i]] = t[i]
            reverse_map[t[i]] = s[i]

    for key, value in swap_map.items():
        if key < value:
            swaps.append((key, value))
        else:
            swaps.append((value, key))

    swaps = list(set(swaps))

    if len(swaps) * 2 != len(swap_map):
        print(-1)
        return

    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

import sys

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    find_swaps(s, t)