def reconstruct_emails(s):
    parts = s.split('@')
    n = len(parts)
    
    if n < 2:
        return "No solution"
    
    result = []
    i = 0
    
    while i < n - 1:
        local = parts[i]
        if not local:
            return "No solution"
        
        j = i + 1
        while j < n - 1 and len(parts[j]) == 0:
            j += 1
        
        if j == n - 1:
            domain = parts[j]
            if not domain:
                return "No solution"
            result.append(local + '@' + domain)
            break
        else:
            domain = parts[j][0]
            result.append(local + '@' + domain)
            parts[j] = parts[j][1:]
            i = j
        
    return ','.join(result)

# Read input
s = input().strip()
print(reconstruct_emails(s))