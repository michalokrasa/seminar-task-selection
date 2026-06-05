def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    s = data[1]
    
    from collections import Counter
    
    # Count the frequency of each character
    freq = Counter(s)
    
    # Find the number of odd frequency characters
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    
    # If there are odd_count odd frequency characters, we need at least odd_count palindromes
    k = max(1, odd_count)
    
    # Calculate the length of each palindrome
    length_of_each_palindrome = n // k
    
    # Prepare to build the palindromes
    half_palindromes = []
    odd_chars = []
    
    # Distribute characters into half_palindromes and odd_chars
    for char, count in freq.items():
        half_palindromes.extend([char] * (count // 2))
        if count % 2 != 0:
            odd_chars.append(char)
    
    # Build the palindromes
    palindromes = []
    half_size = len(half_palindromes)
    
    for i in range(k):
        # Take a slice of half_palindromes
        half = half_palindromes[i * (half_size // k):(i + 1) * (half_size // k)]
        
        # If there are odd characters left, use one in the middle
        if odd_chars:
            middle = odd_chars.pop()
        else:
            middle = ''
        
        # Form the palindrome
        palindrome = ''.join(half) + middle + ''.join(reversed(half))
        palindromes.append(palindrome)
    
    # Output the result
    print(k)
    print(' '.join(palindromes))

main()