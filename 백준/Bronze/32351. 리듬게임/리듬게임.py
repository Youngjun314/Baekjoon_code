n, s, k = map(float, input().split())
m, ans = 1, 0
for i in range(int(k)):
    a, b = map(float, input().split())
    ans += (a - m) * 240 / s
    m = a
    s = b
ans += (n - m + 1) * 240 / s
print(f'{ans:.12f}')