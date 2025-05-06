import sys
n = int(input())
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if (a + b + c) % 2 == 0:
        print('YES')
    else:
        print('NO')