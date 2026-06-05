def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    difficulties = list(map(int, data[2:]))
    
    left = 0
    right = n - 1
    
    while left < n and difficulties[left] <= k:
        left += 1
    
    while right >= 0 and difficulties[right] <= k:
        right -= 1
    
    if left > right:
        print(n)
    else:
        print(left + (n - 1 - right))

main()