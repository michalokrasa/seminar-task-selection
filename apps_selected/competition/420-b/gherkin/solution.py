def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    messages = data[1:m+1]
    
    present = set()
    potential_leaders = set(range(1, n+1))
    
    for message in messages:
        action, id_str = message.split()
        id_num = int(id_str)
        
        if action == '+':
            present.add(id_num)
        elif action == '-':
            if id_num in present:
                present.remove(id_num)
            else:
                potential_leaders.discard(id_num)
    
    potential_leaders -= present
    
    if potential_leaders:
        print(len(potential_leaders))
        print(' '.join(map(str, sorted(potential_leaders))))
    else:
        print(0)

main()