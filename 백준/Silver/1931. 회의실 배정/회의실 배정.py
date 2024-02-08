n = int(input())
l = []
cnt, time = 0, 0
for i in range(n):
    a = list(map(int, input().split()))
    l.append(a)
l.sort(key = lambda x: (x[1], x[0]))
for i in range(n):
    if l[i][0] >= time:
        cnt += 1
        time = l[i][1]
print(cnt)