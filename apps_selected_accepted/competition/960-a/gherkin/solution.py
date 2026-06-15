def can_form_string(s):
    count_a = 0
    count_b = 0
    count_c = 0
    
    for char in s:
        if char == 'a':
            count_a += 1
        elif char == 'b':
            count_b += 1
        elif char == 'c':
            count_c += 1
        else:
            return "NO"
        
        # Check if the order is violated
        if count_b > count_a or count_c > count_a:
            return "NO"
    
    # Check if the number of 'b's and 'c's are valid
    if count_b <= count_a <= count_b + 1 and count_c <= count_a <= count_c + 1:
        return "YES"
    else:
        return "NO"

import sys
input = sys.stdin.read
s = input().strip()
print(can_form_string(s))