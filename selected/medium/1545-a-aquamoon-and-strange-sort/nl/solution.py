def can_be_sorted(n, arr):
    even_indices = arr[0::2]
    odd_indices = arr[1::2]
    
    even_indices_sorted = sorted(even_indices)
    odd_indices_sorted = sorted(odd_indices)
    
    return even_indices == even_indices_sorted and odd_indices == odd_indices_sorted

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
        
        if can_be_sorted(n, arr):
            results.append("YES")
        else:
            results.append("NO")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()