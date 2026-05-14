def crazy_computer(n, c, timestamps):
    if n == 0:
        return 0
    
    count = 1
    for i in range(1, n):
        if timestamps[i] - timestamps[i - 1] > c:
            count = 1
        else:
            count += 1
    return count

# Read input
n, c = map(int, input().split())
timestamps = list(map(int, input().split()))

# Output the result
print(crazy_computer(n, c, timestamps))