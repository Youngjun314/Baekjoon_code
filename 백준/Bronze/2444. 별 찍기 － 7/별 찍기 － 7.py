n = int(input())
for i in range(2 * n - 1):
    for j in range(abs(n - i - 1)):
        print(" ", end = "")
    for j in range(abs(abs(2 * i - 2 * n + 2) - 2 * n + 1)):
        print("*", end = "")
    print("")