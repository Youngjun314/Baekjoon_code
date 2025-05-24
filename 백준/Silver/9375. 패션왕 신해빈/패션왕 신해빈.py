t = int(input())
for i in range(t):
    l = dict()
    n = int(input())
    for j in range(n):
        x, y = map(str, input().split())
        if y in l:
            l[y] += 1
        else:
            l[y] = 1
    ans = 1
    for j in l.values():
        ans *= j + 1
    ans -= 1
    print(ans)