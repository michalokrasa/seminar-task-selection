def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    cards = list(map(int, data[1:]))
    
    from collections import Counter
    card_count = Counter(cards)
    
    for count in card_count.values():
        if count % 2 == 1:
            print("Conan")
            return
    
    print("Agasa")

main()