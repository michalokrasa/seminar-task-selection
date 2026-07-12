t, s, x = map(int, input().split())

if x == t:
    print("YES")
elif x < t:
    print("NO")
else:
    if (x - t) % s == 0 or (x - t - 1) % s == 0 and x != t + 1:
        print("YES")
    else:
        print("NO")