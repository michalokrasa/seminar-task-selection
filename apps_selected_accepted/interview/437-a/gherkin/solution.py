def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    descriptions = {}
    for line in data:
        letter, description = line.split('. ', 1)
        descriptions[letter] = description
    
    lengths = {k: len(v) for k, v in descriptions.items()}
    
    min_length = min(lengths.values())
    max_length = max(lengths.values())
    
    min_count = sum(1 for length in lengths.values() if length == min_length)
    max_count = sum(1 for length in lengths.values() if length == max_length)
    
    if min_count == 1:
        for k, v in lengths.items():
            if v == min_length:
                print(k)
                return
    elif max_count == 1:
        for k, v in lengths.items():
            if v == max_length:
                print(k)
                return
    else:
        print('C')

main()