n = int(input())
ans = 0
l = sorted(list(map(int, input().split())))
for i, j in enumerate(reversed(l)):
    ans += (i + 1) * j
print(ans)