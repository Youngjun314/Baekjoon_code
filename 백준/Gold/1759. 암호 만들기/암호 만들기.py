a, b = map(int, input().split())
l = list(map(str, input().split()))
def f(a, l, l2):
    if a == len(l) and g(l) == 1:
        print(''.join(l))
    else:
        for i in range(len(l2)):
            lx = l[:]
            lx.append(l2[i])
            f(a, lx, l2[i + 1:])
def g(l):
    vowel = set(['a', 'e', 'i', 'o', 'u'])
    constant = set(list('bcdfghjklmnpqrstvwxyz'))
    if len(set(l) & set (vowel)) > 0 and len(set(l) & set (constant)) > 1:
        return 1
    else:
        return 0
l.sort()
for i in range(b - a + 1):
    f(a, [l[i]], l[i + 1:])