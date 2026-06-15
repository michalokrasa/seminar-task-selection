def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    filenames = data[1:n+1]
    delete_indices = list(map(int, data[n+1].split()))
    
    # Get the filenames to be deleted
    to_delete = [filenames[i-1] for i in delete_indices]
    
    # Check if all filenames to be deleted have the same length
    length = len(to_delete[0])
    for filename in to_delete:
        if len(filename) != length:
            print("No")
            return
    
    # Create a pattern based on the files to be deleted
    pattern = list(to_delete[0])
    for i in range(length):
        for filename in to_delete:
            if filename[i] != pattern[i]:
                pattern[i] = '?'
                break
    
    # Convert pattern list to string
    pattern = ''.join(pattern)
    
    # Check if the pattern matches any file that should not be deleted
    for i in range(n):
        if i+1 not in delete_indices:
            if len(filenames[i]) == length:
                match = True
                for j in range(length):
                    if pattern[j] != '?' and pattern[j] != filenames[i][j]:
                        match = False
                        break
                if match:
                    print("No")
                    return
    
    # If no conflicts, print the pattern
    print("Yes")
    print(pattern)
