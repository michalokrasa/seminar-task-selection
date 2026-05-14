def reverse_integer(n):
    # Convert the input to a string and strip leading zeros
    s = str(n).lstrip('0')
    
    # Check if the number is negative
    if s.startswith('-'):
        # Reverse the digits after the negative sign and prepend the negative sign
        reversed_number = '-' + s[:0:-1]
    else:
        # Reverse the digits
        reversed_number = s[::-1]
    
    # Convert the reversed string back to an integer to remove any leading zeros
    return int(reversed_number)

if __name__ == "__main__":
    import sys
    input_number = sys.stdin.read().strip()
    print(reverse_integer(input_number))