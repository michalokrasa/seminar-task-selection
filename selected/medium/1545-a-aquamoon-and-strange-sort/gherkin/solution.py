def can_sort_with_adjacent_swaps(n, sequence):
    # Separate the sequence into even and odd indexed elements
    even_indexed = sequence[::2]
    odd_indexed = sequence[1::2]
    
    # Sort both parts
    even_indexed.sort()
    odd_indexed.sort()
    
    # Merge them back into a single sorted sequence
    sorted_sequence = []
    for i in range(n):
        if i % 2 == 0:
            sorted_sequence.append(even_indexed[i // 2])
        else:
            sorted_sequence.append(odd_indexed[i // 2])
    
    # Check if the merged sequence is sorted
    return sorted_sequence == sorted(sequence)

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
        sequence = list(map(int, data[index:index + n]))
        index += n
        
        if can_sort_with_adjacent_swaps(n, sequence):
            results.append("YES")
        else:
            results.append("NO")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()