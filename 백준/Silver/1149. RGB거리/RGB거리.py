n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l2 = [[0] * 3 for _ in range(n)]

l2[0][0] = l[0][0]  
l2[0][1] = l[0][1]  
l2[0][2] = l[0][2] 

for i in range(1, n):
    l2[i][0] = min(l2[i-1][1], l2[i-1][2]) + l[i][0]
    l2[i][1] = min(l2[i-1][0], l2[i-1][2]) + l[i][1]
    l2[i][2] = min(l2[i-1][0], l2[i-1][1]) + l[i][2]

print(min(l2[n-1]))
