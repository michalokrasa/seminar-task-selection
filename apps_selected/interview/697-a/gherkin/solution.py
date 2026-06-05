t, s, x = map(int, input().split())

if x < t:
    print("NO")
elif x == t:
    print("YES")
else:
    if (x - t) % s == 0 or ((x - t) % s == 1 and x != t + 1):
        print("YES")
    else:
        print("NO")