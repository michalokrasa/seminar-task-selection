def detect_language(sentence):
    if sentence.endswith("po"):
        return "FILIPINO"
    elif sentence.endswith("desu") or sentence.endswith("masu"):
        return "JAPANESE"
    elif sentence.endswith("mnida"):
        return "KOREAN"
    return "UNKNOWN"

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        sentence = data[i]
        results.append(detect_language(sentence))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()