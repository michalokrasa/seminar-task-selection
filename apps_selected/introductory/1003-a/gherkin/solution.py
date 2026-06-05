def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    coins = list(map(int, data[1:]))
    
    from collections import Counter
    coin_count = Counter(coins)
    
    # The minimum number of pockets needed is the maximum frequency of any coin value
    max_frequency = max(coin_count.values())
    
    print(max_frequency)

main()