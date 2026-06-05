n = int(input().strip())
s = input().strip()

def count_changeable_positions(n, s):
    balance = 0
    min_balance = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)
    
    if balance != 0:
        return 0
    
    return -min_balance

print(count_changeable_positions(n, s))