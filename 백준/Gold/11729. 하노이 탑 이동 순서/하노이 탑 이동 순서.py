n = int(input())
print(2 ** n - 1)
def f(n, a, b):
    if n < 2:
        print(a, b)
    else:
        f(n - 1, a, 6 - a - b)
        f(1, a, b)
        f(n - 1, 6 - a - b, b)
f(n, 1, 3)