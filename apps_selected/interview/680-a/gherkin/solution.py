def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().strip().split()))
    
    from collections import Counter
    
    # Count the occurrences of each card number
    count = Counter(data)
    
    # Calculate the total sum of all cards
    total_sum = sum(data)
    
    # Initialize the minimum sum as the total sum (no cards discarded)
    min_sum = total_sum
    
    # Check for each card number if we can discard 2 or 3 cards
    for num, cnt in count.items():
        if cnt >= 2:
            # Try discarding two cards of this number
            min_sum = min(min_sum, total_sum - 2 * num)
        if cnt >= 3:
            # Try discarding three cards of this number
            min_sum = min(min_sum, total_sum - 3 * num)
    
    # Output the minimum sum of remaining cards
    print(min_sum)

main()