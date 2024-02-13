l = []
t = int(input())
lnt = 0
for i in range(t):
    a = list(input())
    l = []
    lnt = 0
    for i in a:
        if lnt == 0:
            l.append(i)
            lnt += 1
        elif l[lnt - 1] == '(':
            if i == '(':
                l.append('(')
                lnt += 1 
            else:
                l.pop()
                lnt -= 1
        else:
            l.append(i)
            lnt += 1
    if l == []:
        print('YES')
    else:
        print('NO')