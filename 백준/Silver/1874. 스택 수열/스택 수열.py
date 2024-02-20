n = int(input())
l, stack, out = [], [], []
lnt, llnt, cnt = 0, n, 1
for i in range(n):
    a = int(input())
    l.append(a)
l.reverse()
while l != []:
    if lnt == 0:
        stack.append(cnt)
        lnt += 1
        cnt += 1
        out.append('+')
    elif stack[lnt - 1] == l[llnt - 1]:
        stack.pop()
        l.pop()
        lnt -= 1
        llnt -= 1
        out.append('-')
    elif cnt > n:
        out = ['NO']
        break
    else:
        stack.append(cnt)
        lnt += 1
        cnt += 1
        out.append('+')
for i in out:
    print(i)