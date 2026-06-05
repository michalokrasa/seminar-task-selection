n = int(input().strip())
mishka_wins = 0
chris_wins = 0

for _ in range(n):
    m_i, c_i = map(int, input().strip().split())
    if m_i > c_i:
        mishka_wins += 1
    elif c_i > m_i:
        chris_wins += 1

if mishka_wins > chris_wins:
    print("Mishka")
elif chris_wins > mishka_wins:
    print("Chris")
else:
    print("Friendship is magic!^^")