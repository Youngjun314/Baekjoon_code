import sys

input = sys.stdin.readline

stack = []
n = int(input().rstrip())
length = 0
for i in range(n):
    a = str(input().rstrip())
    if a == 'pop':
        if length == 0:
            print('-1')
        else:
            print(stack.pop())
            length -= 1
    elif a == 'size':
        print(length)
    elif a == 'empty':
        if length == 0:
            print('1')
        else:
            print('0')
    elif a == 'top':
        if length == 0:
            print('-1')
        else:
            print(stack[length - 1])
    else:
        stack.append(a[5:])
        length += 1