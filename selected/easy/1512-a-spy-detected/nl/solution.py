def find_unique_index(n, arr):
    if arr[0] != arr[1] and arr[0] != arr[2]:
        return 1
    for i in range(1, n):
        if arr[i] != arr[0]:
            return i + 1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        results.append(find_unique_index(n, arr))
    
    for result in results:
        print(result)

main()