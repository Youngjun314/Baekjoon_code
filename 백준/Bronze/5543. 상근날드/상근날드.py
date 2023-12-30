min1 = 2000
min2 = 2000
for i in range(3):
    a = int(input())
    if a < min1:
        min1 = a
for i in range(2):
    a = int(input())
    if a < min2:
        min2 = a
print (min1 + min2 - 50)