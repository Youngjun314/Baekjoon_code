n = int(input())
l = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if i + 1 in l:
        del l[:l.index(i + 1) + 1]
        cnt += 1
    else:
        break
print(n - cnt)