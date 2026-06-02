def find_unique_index(n, arr):
    # Using a dictionary to count occurrences
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Find the unique element
    unique_element = None
    for num, cnt in count.items():
        if cnt == 1:
            unique_element = num
            break
    
    # Find the 1-based index of the unique element
    for i in range(n):
        if arr[i] == unique_element:
            return i + 1

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
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

if __name__ == "__main__":
    main()