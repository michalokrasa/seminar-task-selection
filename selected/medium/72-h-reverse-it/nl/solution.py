def reverse_integer(s):
    # Strip leading zeros and handle negative sign
    if s[0] == '-':
        reversed_number = '-' + s[:0:-1].lstrip('0')
    else:
        reversed_number = s[::-1].lstrip('0')
    
    # Handle the case where the result is an empty string
    if reversed_number == '' or reversed_number == '-':
        return '0'
    
    return reversed_number

# Read input
input_number = input().strip()

# Output the reversed integer
print(reverse_integer(input_number))