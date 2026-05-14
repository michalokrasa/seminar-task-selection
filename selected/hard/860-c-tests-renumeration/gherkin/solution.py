def generate_move_script(n, files):
    examples = []
    regulars = []
    
    for name, typ in files:
        if typ == 1:
            examples.append(name)
        else:
            regulars.append(name)
    
    e = len(examples)
    moves = []
    temp_name = "temp"
    
    # Create a map for the target names
    target_names = {}
    for i, name in enumerate(examples, 1):
        target_names[name] = str(i)
    for i, name in enumerate(regulars, e + 1):
        target_names[name] = str(i)
    
    # To avoid overwriting, we need to use a temporary name
    used_names = set(target_names.values())
    
    # Perform the moves
    for name, target in target_names.items():
        if name != target:
            if target in target_names:
                # If the target is also a source, use a temporary name
                while temp_name in used_names:
                    temp_name += "_"
                moves.append(f"move {target} {temp_name}")
                used_names.add(temp_name)
                target_names[target] = temp_name
            
            moves.append(f"move {name} {target}")
            used_names.add(target)
    
    return moves

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n = int(data[0])
    files = []
    for line in data[1:n+1]:
        name, typ = line.split()
        files.append((name, int(typ)))
    
    moves = generate_move_script(n, files)
    print(len(moves))
    for move in moves:
        print(move)

if __name__ == "__main__":
    main()