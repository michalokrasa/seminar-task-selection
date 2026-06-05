def main():
    import sys
    input = sys.stdin.read
    S = input().strip()
    
    # Count the number of 'a's, 'b's, and 'c's
    count_a = 0
    count_b = 0
    count_c = 0
    
    # State machine to track the current section of the string
    state = 'a'  # Start with 'a's
    
    for char in S:
        if state == 'a':
            if char == 'a':
                count_a += 1
            elif char == 'b':
                state = 'b'
                count_b += 1
            else:
                print("NO")
                return
        elif state == 'b':
            if char == 'b':
                count_b += 1
            elif char == 'c':
                state = 'c'
                count_c += 1
            else:
                print("NO")
                return
        elif state == 'c':
            if char == 'c':
                count_c += 1
            else:
                print("NO")
                return
    
    # Check if the number of 'c's is equal to the number of 'a's or 'b's
    if count_c == count_a or count_c == count_b:
        print("YES")
    else:
        print("NO")

main()