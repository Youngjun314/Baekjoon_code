n = int(input())
m = round((2 * n) ** (1 / 2) + 1)
if m % 2 == 0:
    print(m - n + ((m - 1) * (m - 2) // 2), n - ((m - 1) * (m - 2) // 2), sep = '/')
else:
    print(n - ((m - 1) * (m - 2) // 2), m - n + ((m - 1) * (m - 2) // 2), sep = '/')