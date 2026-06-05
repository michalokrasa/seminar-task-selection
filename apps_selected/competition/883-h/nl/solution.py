def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    from collections import Counter
    
    # Count the frequency of each character
    freq = Counter(s)
    
    # Find the maximum number of palindromes we can form
    # by checking the number of odd frequency characters
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    
    # If there are odd frequency characters, we need at least that many palindromes
    # Otherwise, we can form a single palindrome
    k = max(1, odd_count)
    
    # Calculate the length of each palindrome
    length_of_each_palindrome = n // k
    
    # Prepare to form the palindromes
    half_palindrome = []
    odd_chars = []
    
    # Distribute characters to form palindromes
    for char, count in freq.items():
        # Add pairs of characters to half_palindrome
        half_palindrome.extend([char] * (count // 2))
        # If there's an odd character, add it to odd_chars
        if count % 2 != 0:
            odd_chars.append(char)
    
    # Prepare the result palindromes
    palindromes = []
    
    # We need k palindromes
    for i in range(k):
        # Start forming the palindrome
        left_half = []
        
        # Fill the left half of the palindrome
        for _ in range(length_of_each_palindrome // 2):
            if half_palindrome:
                left_half.append(half_palindrome.pop())
        
        # If the palindrome length is odd, add an odd character in the middle
        if length_of_each_palindrome % 2 != 0:
            if odd_chars:
                middle_char = odd_chars.pop()
            else:
                middle_char = half_palindrome.pop()
            palindrome = left_half + [middle_char] + left_half[::-1]
        else:
            palindrome = left_half + left_half[::-1]
        
        palindromes.append(''.join(palindrome))
    
    # Output the result
    print(k)
    print(' '.join(palindromes))

main()