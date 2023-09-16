day = int(input())
a = list(map(int,input().split( )))
n = 0
for i in range(5):
    if a[i] == day:
        n += 1
print(n)