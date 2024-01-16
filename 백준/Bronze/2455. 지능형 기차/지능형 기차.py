cnt = 0
maxm = 0
for i in range(4):
    a, b = map(int, input().split())
    cnt -= a
    cnt += b
    if cnt > maxm:
        maxm = cnt
print (maxm)
