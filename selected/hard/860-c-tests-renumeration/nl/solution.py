def renumber_tests(n, files):
    example_files = []
    regular_files = []
    name_to_index = {}
    
    for i, (name, type_) in enumerate(files):
        name_to_index[name] = i
        if type_ == 1:
            example_files.append(name)
        else:
            regular_files.append(name)
    
    e = len(example_files)
    target_names = [str(i + 1) for i in range(n)]
    
    moves = []
    used_temp_names = set()
    
    def get_temp_name():
        for i in range(1, n + 1):
            temp_name = f"t{i}"
            if temp_name not in name_to_index and temp_name not in used_temp_names:
                used_temp_names.add(temp_name)
                return temp_name
        raise RuntimeError("Ran out of temporary names")
    
    for i in range(e):
        current_name = example_files[i]
        target_name = target_names[i]
        if current_name != target_name:
            if target_name in name_to_index:
                temp_name = get_temp_name()
                moves.append(f"move {target_name} {temp_name}")
                name_to_index[temp_name] = name_to_index.pop(target_name)
            moves.append(f"move {current_name} {target_name}")
            name_to_index[target_name] = name_to_index.pop(current_name)
    
    for i in range(e, n):
        current_name = regular_files[i - e]
        target_name = target_names[i]
        if current_name != target_name:
            if target_name in name_to_index:
                temp_name = get_temp_name()
                moves.append(f"move {target_name} {temp_name}")
                name_to_index[temp_name] = name_to_index.pop(target_name)
            moves.append(f"move {current_name} {target_name}")
            name_to_index[target_name] = name_to_index.pop(current_name)
    
    return moves

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    files = [line.split() for line in data[1:]]
    files = [(name, int(type_)) for name, type_ in files]
    
    moves = renumber_tests(n, files)
    
    print(len(moves))
    for move in moves:
        print(move)

if __name__ == "__main__":
    main()