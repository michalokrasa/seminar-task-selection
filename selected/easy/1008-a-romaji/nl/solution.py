def is_berlanese(word):
    vowels = {'a', 'o', 'u', 'i', 'e'}
    n = len(word)
    
    for i in range(n):
        if word[i] not in vowels:
            if word[i] != 'n':
                if i == n - 1 or word[i + 1] not in vowels:
                    return "NO"
    return "YES"

# Read input
s = input().strip()
# Output result
print(is_berlanese(s))