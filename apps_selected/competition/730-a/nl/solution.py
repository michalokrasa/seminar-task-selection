def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    ratings = list(map(int, data[1:]))
    
    min_rating = min(ratings)
    max_rating = max(ratings)
    
    # We will try to equalize to the highest possible rating
    # Start from max_rating and go downwards
    for target in range(max_rating, min_rating - 1, -1):
        # Calculate how many matches are needed to bring everyone to 'target'
        matches = []
        for i in range(n):
            if ratings[i] > target:
                matches_needed = ratings[i] - target
                for _ in range(matches_needed):
                    matches.append(i)
        
        # Check if we can form valid matches with the indices in 'matches'
        if len(matches) % 2 == 0 or len(matches) % 3 == 0 or len(matches) % 4 == 0 or len(matches) % 5 == 0:
            # We can form valid matches
            print(target)
            print(len(matches) // 2)
            for i in range(0, len(matches), 2):
                match = ['0'] * n
                match[matches[i]] = '1'
                match[matches[i+1]] = '1'
                print(''.join(match))
            return
    
    # If we reach here, it means we can only equalize to the minimum rating
    print(min_rating)
    print(0)

main()