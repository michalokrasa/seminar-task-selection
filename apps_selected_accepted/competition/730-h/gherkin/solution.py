def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    filenames = data[1:n+1]
    indices = list(map(int, data[n+1].split()))
    
    # Convert indices to zero-based
    indices = [i - 1 for i in indices]
    
    # Get the files to be deleted
    to_delete = [filenames[i] for i in indices]
    
    # Check if all files to be deleted have the same length
    length = len(to_delete[0])
    if not all(len(f) == length for f in to_delete):
        print("No")
        return
    
    # Create a pattern
    pattern = list(to_delete[0])
    
    for i in range(1, len(to_delete)):
        for j in range(length):
            if pattern[j] != to_delete[i][j]:
                pattern[j] = '?'
    
    # Check if the pattern matches only the files to be deleted
    pattern = ''.join(pattern)
    
    for i in range(n):
        if i in indices:
            # File should match the pattern
            if not match(filenames[i], pattern):
                print("No")
                return
        else:
            # File should not match the pattern
            if match(filenames[i], pattern):
                print("No")
                return
    
    print("Yes")
    print(pattern)

def match(filename, pattern):
    if len(filename) != len(pattern):
        return False
    for f, p in zip(filename, pattern):
        if p != '?' and f != p:
            return False
    return True

main()