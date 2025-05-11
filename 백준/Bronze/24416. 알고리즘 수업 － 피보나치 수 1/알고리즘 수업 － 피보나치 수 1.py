n = int(input())
cnta, cntb = 0, 0
f = [0] * (n + 1)
for i in range(1, n + 1):
    if i <= 2:
        f[i] = 1
    else:
        f[i] = f[i - 1] + f[i - 2]
        cntb += 1
cnta = f[n]
print(cnta, cntb)