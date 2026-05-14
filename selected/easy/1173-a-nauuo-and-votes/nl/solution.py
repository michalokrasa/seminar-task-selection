def nauuo_and_votes(x, y, z):
    if x > y + z:
        return "+"
    elif y > x + z:
        return "-"
    elif x == y and z == 0:
        return "0"
    else:
        return "?"

# Read input
x, y, z = map(int, input().split())

# Output the result
print(nauuo_and_votes(x, y, z))