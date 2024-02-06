n = int(input())
l = list(map(int, input().split()))
l.sort
cnt = 0
index = 0
for i in range(n):
    if i + 1 in l and index <= l.index(i + 1):
        cnt += 1
        index = l.index(i + 1)
    else:
        break
print(n - cnt)