def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    logs = data[1:]
    
    present = set()
    potential_leaders = set(range(1, n + 1))
    
    for log in logs:
        action, id_str = log.split()
        id = int(id_str)
        
        if action == '+':
            present.add(id)
        elif action == '-':
            present.remove(id)
        
        if present:
            potential_leaders.intersection_update(present)
    
    potential_leaders = sorted(potential_leaders)
    
    print(len(potential_leaders))
    if potential_leaders:
        print(' '.join(map(str, potential_leaders)))

main()