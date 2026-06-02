def is_berlanese_valid(word):
    vowels = {'a', 'o', 'u', 'i', 'e'}
    n = len(word)
    
    for i in range(n):
        if word[i] not in vowels and word[i] != 'n':
            if i == n - 1 or word[i + 1] not in vowels:
                return "NO"
    
    return "YES"

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    word = input().strip()
    print(is_berlanese_valid(word))