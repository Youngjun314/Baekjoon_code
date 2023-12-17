d = dict()
a = input().upper()
for i in a:
    if i in list(d.keys()):
        d[i] += 1
    else:
        d[i] = 1
maxk, maxv, n = 0, -1, 0
for k, v in d.items():
    if v > maxv:
        maxv = v 
        maxk = k 
        n = 0
    elif v == maxv:
        n = 1
if n == 0:
    print(maxk.upper())
else:
    print('?')