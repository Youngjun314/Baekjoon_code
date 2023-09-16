n, k = map(int,input().split())
l = []
a = []
for i in range(n):
    l.append(i + 1)
for i in range(n - 1):
    for i in range(k - 1):
        l.append(l[0])
        l.remove(l[0])
    a.append(l[0])
    l.remove(l[0])
    #a.append(l[(k - 1) % len(l)])
    #l.remove(l[(k - 1) % len(l)])
    
a.append(l[0])
print('<', end = '')
for i in a[:-1]:
    print(i,', ', sep = '', end = '')
print(a[-1], end = '')
print('>')

    

