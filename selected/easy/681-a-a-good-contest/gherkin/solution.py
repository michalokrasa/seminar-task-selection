def good_performance_check():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n = int(data[0])
    for i in range(1, n + 1):
        handle, before, after = data[i].split()
        before = int(before)
        after = int(after)
        
        if before >= 2400 and after > before:
            print("YES")
            return
    
    print("NO")

good_performance_check()