l = []
while True:
    a = list(map(int, input().split()))
    if a == [0, 0, 0]:
        break
    else:
        l.append(a)
for i in range(len(l)):
    print('Case', str(i + 1) + ':', l[i][2] // l[i][1] * l[i][0] + min(l[i][2] % l[i][1], l[i][0]))
