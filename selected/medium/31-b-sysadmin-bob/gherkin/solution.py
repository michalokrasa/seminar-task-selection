def reconstruct_emails(s):
    parts = s.split('@')
    n = len(parts)
    
    if n < 2:
        return "No solution"
    
    result = []
    for i in range(n - 1):
        if len(parts[i]) == 0 or len(parts[i + 1]) == 0:
            return "No solution"
        if i < n - 2:
            result.append(parts[i] + '@' + parts[i + 1][0])
            parts[i + 1] = parts[i + 1][1:]
        else:
            result.append(parts[i] + '@' + parts[i + 1])
    
    if any(len(part) == 0 for part in parts):
        return "No solution"
    
    return ','.join(result)

if __name__ == "__main__":
    import sys
    input_string = sys.stdin.read().strip()
    print(reconstruct_emails(input_string))