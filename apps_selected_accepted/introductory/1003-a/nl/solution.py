def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    coins = list(map(int, data[1:]))
    
    from collections import Counter
    coin_count = Counter(coins)
    
    max_count = max(coin_count.values())
    
    print(max_count)

main()