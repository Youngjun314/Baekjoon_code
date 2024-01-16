n, m = map(int,input().split())
l, l2 = [], []
for i in range(n):
    row = list(map(int, input().split()))
    l.append(row)
for i in range(n):
    row = list(map(int, input().split()))
    l2.append(row)
for i in range(n):
    for j in range(m):
        print (l[i][j] + l2[i][j], end = ' ')
    print('')