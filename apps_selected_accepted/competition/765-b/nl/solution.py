def main():
    import sys
    input = sys.stdin.read
    S = input().strip()
    
    # Dictionary to map original characters to obfuscated ones
    char_map = {}
    next_char = 'a'
    
    for char in S:
        if char not in char_map:
            if next_char > 'z':
                print("NO")
                return
            char_map[char] = next_char
            next_char = chr(ord(next_char) + 1)
    
    # Check if the transformation is consistent
    transformed = ''.join(char_map[char] for char in S)
    if transformed == S:
        print("YES")
    else:
        print("NO")

main()