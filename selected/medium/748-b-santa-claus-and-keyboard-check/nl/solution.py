def find_swaps(s, t):
    if len(s) != len(t):
        return -1

    mapping_s_to_t = {}
    mapping_t_to_s = {}
    swaps = set()

    for char_s, char_t in zip(s, t):
        if char_s in mapping_s_to_t:
            if mapping_s_to_t[char_s] != char_t:
                return -1
        if char_t in mapping_t_to_s:
            if mapping_t_to_s[char_t] != char_s:
                return -1

        mapping_s_to_t[char_s] = char_t
        mapping_t_to_s[char_t] = char_s

    for char_s, char_t in mapping_s_to_t.items():
        if char_s != char_t:
            swaps.add(tuple(sorted((char_s, char_t))))

    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

# Read input
s = input().strip()
t = input().strip()

# Find and print swaps
find_swaps(s, t)