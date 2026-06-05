def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    ratings = list(map(int, data[1:n+1]))
    
    # Calculate the minimum rating
    min_rating = min(ratings)
    
    # Calculate the number of matches needed
    matches = []
    for i in range(n):
        while ratings[i] > min_rating:
            # Find a group of friends to play a match
            match = ['0'] * n
            match[i] = '1'
            count = 1
            for j in range(n):
                if i != j and ratings[j] > min_rating and count < 5:
                    match[j] = '1'
                    count += 1
            matches.append(''.join(match))
            for j in range(n):
                if match[j] == '1':
                    ratings[j] -= 1
    
    # Output the results
    print(min_rating)
    print(len(matches))
    for match in matches:
        print(match)

main()