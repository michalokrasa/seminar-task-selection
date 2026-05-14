def is_good_contest(n, participants):
    for handle, before, after in participants:
        if int(before) >= 2400 and int(after) > int(before):
            return "YES"
    return "NO"

# Read input
n = int(input().strip())
participants = [input().strip().split() for _ in range(n)]

# Output result
print(is_good_contest(n, participants))