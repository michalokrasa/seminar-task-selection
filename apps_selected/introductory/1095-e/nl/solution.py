def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    if n % 2 != 0:
        print(0)
        return
    
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)
    
    if balance != 0:
        print(0)
        return
    
    # Count the number of positions that can be changed
    # to make the sequence regular
    count = 0
    balance = 0
    for i in range(n):
        if s[i] == '(':
            balance += 1
        else:
            balance -= 1
        
        if balance < 0:
            if s[i] == ')':
                count += 1
            balance += 2  # Simulate changing ')' to '('
    
    print(count)
