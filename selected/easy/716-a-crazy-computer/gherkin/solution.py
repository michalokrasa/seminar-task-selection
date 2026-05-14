def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    c = int(data[1])
    timestamps = list(map(int, data[2:]))
    
    if n == 0:
        print(0)
        return
    
    remaining_words = 1
    for i in range(1, n):
        if timestamps[i] - timestamps[i - 1] > c:
            remaining_words = 1
        else:
            remaining_words += 1
    
    print(remaining_words)

if __name__ == "__main__":
    main()