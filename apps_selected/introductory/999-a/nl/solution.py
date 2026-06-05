def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    problems = list(map(int, data[2:]))
    
    left = 0
    right = n - 1
    
    # Solve from the left
    while left <= right and problems[left] <= k:
        left += 1
    
    # Solve from the right
    while right >= left and problems[right] <= k:
        right -= 1
    
    # Total problems solved is the sum of problems solved from both ends
    solved = left + (n - 1 - right)
    
    print(solved)
