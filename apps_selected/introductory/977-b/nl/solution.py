def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    two_gram_count = {}
    
    for i in range(n - 1):
        two_gram = s[i:i+2]
        if two_gram in two_gram_count:
            two_gram_count[two_gram] += 1
        else:
            two_gram_count[two_gram] = 1
    
    most_frequent_two_gram = max(two_gram_count, key=two_gram_count.get)
    
    print(most_frequent_two_gram)
